"""Cổng phòng ngừa (guards) của bàn: chạy TRƯỚC khi model đọc ticket và TRƯỚC mỗi lệnh ghi.

Đây là chỗ chính để Kỹ sư cổng sửa ở vòng 1 (phút 85-105) và vòng 2 (sau thẻ sự cố).
"""
from __future__ import annotations

from . import helpers as H
from .tools import Verdict


def pre_guard(ctx) -> Verdict:
    """Chạy MỘT lần trước khi trợ lý đọc ticket.

    Các câu trả lời hợp lệ:
        Verdict.allow()
        Verdict.allow(policy_id="...")
        Verdict.deny("lý do")
        Verdict.escalate("lý do")
        Verdict.rewrite("lý do", "nội dung mới")
    """
    return Verdict.allow()


def _resolve_parcel(parcels, parcel_id, as_of):
    if parcel_id:
        return next((parcel for parcel in parcels if parcel["parcel_id"] == parcel_id), None)
    if len(parcels) == 1:
        return parcels[0]
    delayed = [parcel for parcel in parcels if H.db_delay_days(parcel, as_of) > 0]
    return delayed[0] if len(delayed) == 1 else None


def _db_order_context(ctx, action):
    order = ctx.tools.lookup_order(action.get("order_id"))
    if not order:
        return None, None, None, None
    parcel = _resolve_parcel(order["parcels"], ctx.ticket.get("parcel_id"), ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of) if parcel else 0
    return order, parcel, policy, delay


def write_gate(ctx, action) -> Verdict:
    """Chạy TRƯỚC MỖI lệnh ghi: issue_refund, file_carrier_fault, notify_carrier, send_reply."""
    tool = action.get("tool")

    # Cổng 1: Kiểm tra kiện và quyền lợi từ tracking trước khi ghi hoàn tiền.
    if tool == "issue_refund":
        order, parcel, policy, delay = _db_order_context(ctx, action)
        if order and parcel is None:
            return Verdict.escalate("Không xác định được kiện cần hoàn tiền theo tracking, chuyển người duyệt")
        if parcel and policy:
            expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
            amount = action.get("amount_vnd", 0)
            if len(order["parcels"]) > 1 and amount != expected:
                return Verdict.escalate("Số tiền hoàn không khớp quyền lợi của kiện được xác định")
            if amount > expected and not action.get("approval_id"):
                return Verdict.escalate("Số tiền hoàn vượt quyền lợi theo tracking DB, chuyển người duyệt")

        # Cổng 2: Chặn vượt trần hoàn tự động trong ngày theo config
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if cap is not None and not action.get("approval_id"):
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + action.get("amount_vnd", 0) > cap:
                return Verdict.escalate("Vượt trần hoàn tự động trong ngày, chuyển người duyệt")

    # Cổng 3: Ghi theo kiện trong tracking và giới hạn số lỗi tự động của mỗi hãng.
    if tool == "file_carrier_fault":
        _, parcel, policy, delay = _db_order_context(ctx, action)
        if not parcel or not policy or not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Tracking DB chưa đủ căn cứ ghi lỗi hãng cho kiện này")

        carrier_id = parcel["carrier_id"]
        cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if cap is not None and len(ctx.tools.fault_rows(carrier_id=carrier_id)) >= cap:
            return Verdict.deny("Hãng đã chạm trần lỗi tự động trong ngày, cần người duyệt trước khi ghi thêm")

        attribution = {
            "parcel_id": parcel["parcel_id"],
            "carrier_id": carrier_id,
            "driver_id": parcel.get("driver_id"),
            "delay_days": delay,
        }
        if any(action.get(key) != value for key, value in attribution.items()):
            return Verdict.modify("Đối chiếu kiện, hãng, tài xế và số ngày trễ theo tracking", **attribution)

    # Cổng 4: Loại bỏ trường PII / ghi chú tự do của khách trước khi gửi cho hãng vận chuyển
    if tool == "notify_carrier":
        blocked = set((ctx.gates or {}).get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
        payload = dict(action.get("payload") or {})
        removed = [k for k in list(payload.keys()) if k in blocked]
        if removed:
            for k in removed:
                payload.pop(k, None)
            return Verdict.modify("Loại bỏ trường PII/ghi chú tự do khỏi payload gửi hãng", payload=payload)

    return Verdict.allow()
