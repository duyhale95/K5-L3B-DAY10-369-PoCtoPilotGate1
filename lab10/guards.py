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


def _db_order_context(ctx, action):
    order_id = action.get("order_id")
    if not order_id:
        return None, None, None, None
    order = ctx.tools.lookup_order(order_id)
    if not order:
        return None, None, None, None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of) if parcel else 0
    return order, parcel, policy, delay


def write_gate(ctx, action) -> Verdict:
    """Chạy TRƯỚC MỖI lệnh ghi: issue_refund, file_carrier_fault, notify_carrier, send_reply."""
    tool = action.get("tool")

    # Cổng 1: Chặn hoàn tiền vượt quyền lợi tính từ tracking DB (trừ khi có approval_id)
    if tool == "issue_refund":
        order, parcel, policy, delay = _db_order_context(ctx, action)
        if order and parcel and policy and not action.get("approval_id"):
            expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
            if action.get("amount_vnd", 0) > expected:
                return Verdict.escalate("Số tiền hoàn vượt quyền lợi theo tracking DB, chuyển người duyệt")

        # Cổng 2: Chặn vượt trần hoàn tự động trong ngày theo config
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if cap is not None and not action.get("approval_id"):
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + action.get("amount_vnd", 0) > cap:
                return Verdict.escalate("Vượt trần hoàn tự động trong ngày, chuyển người duyệt")

    # Cổng 3: Chặn ghi lỗi hãng khi tracking DB chưa đủ điều kiện lỗi hãng
    if tool == "file_carrier_fault":
        order, parcel, policy, delay = _db_order_context(ctx, action)
        if order and parcel and policy:
            if not H.carrier_at_fault(policy, parcel, delay):
                return Verdict.escalate("Tracking DB chưa đủ điều kiện lỗi hãng, chuyển người duyệt")

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
