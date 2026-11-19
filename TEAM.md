# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `369`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-369-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S6`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Hà Lê Duy | 2A202603851 | Sản phẩm và kinh doanh | x |
|   2 | Nguyễn Thiên Bảo | 2A202603861 | Kỹ sư cổng | |
|   3 | Nguyễn Hoàng Gia An | 2A202603799 | Vận hành và pháp lý | |
|   4 | | | | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên:
`["HaLeDuy-2A202603851", "NguyenThienBao-2A202603861", "NguyenHoangGiaAn-2A202603799"]`

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HaLeDuy-2A202603851

### Phần việc phụ trách

Trưởng nhóm · Vai **Sản phẩm và kinh doanh**: lập kế hoạch chia việc 3 thành viên (CP1–CP5), phụ trách Phiếu A (Câu 1.1, 1.5, 1.6), `config/acceptance_criteria.json`, Phiếu B (Câu 2.3 bản đồ dữ liệu & drift, Câu 2.9 `business` trong `config/operating_gates.json`, phần kinh doanh trong B8).

### Đóng góp cụ thể

- Cấu hình repo, bảng thành viên `TEAM.md`, lập `PLAN.md` phân công 3 vai không xung đột Git.
- Hoàn thiện Phiếu A và ký `config/acceptance_criteria.json` (`6e4f816`) trước khi chạy đánh giá.
- Hoàn thiện bản đồ dữ liệu, drift, cổng `business` vòng 1 và chốt Gate v1 (Phiếu B).
- Kéo thẻ sự cố `S6` (`0d86d8d`), review & merge PR #1–#4, hoàn thiện C0–C1, C5, kiểm tra đồng bộ `submission/` và gom bài cuối.

### Bằng chứng

- Commit `6e4f816` (`Sign acceptance criteria`), `0540a49` (v1), `0d86d8d` (`Nhan the S6`), `583a441` (PR #1), `a174095` (PR #2), `0eba096` (PR #4).
- `templates/form-a-criteria.md`, `config/acceptance_criteria.json`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`, báo cáo `R-S6-grade-20261119-173149-704885`.

### Exit ticket

- **Một điều học được:** Phải ký tiêu chí chấp nhận trước khi chạy đo, và luôn kiểm soát rủi ro ở cấp hệ thống (cổng code, ngưỡng kinh doanh, vận hành, pháp lý) thay vì chỉ tin vào model; đặc biệt trên S6 khi tách kiện thì đơn vị chịu lỗi là `parcel_id` chứ không phải `order_id`.
- **Một điều còn chưa chắc:** Trên dữ liệu pilot thật, độ trễ cập nhật tracking sau bàn giao đa kiện và tỉ lệ đơn không xác định kho (`?`) có làm thay đổi chi phí/ticket và SLA 60 phút vào giờ cao điểm hay không.
- **Ghi nhận dùng AI:** Dùng trợ lý AI (Antigravity) để lập kế hoạch `PLAN.md`, soát config/rubric, rà soát PR của thành viên, tổng hợp Phiếu A/B/C và kiểm tra tính toàn vẹn bài nộp.

## NguyenThienBao-2A202603861

### Phần việc phụ trách

Vai **Kỹ sư cổng**: Câu 1.3 (offline metric), chạy các lệnh CLI (`eval`, `trace`, `gate`, `checkpoint`, `grade`), Câu 2.1–2.2 (baseline & soát lỗi `T-002@55`), Câu 2.6–2.8 (code cổng vòng 1 trong `lab10/guards.py`, tránh rò rỉ dữ liệu, behavioral test `--adhoc`), và vòng 2 sửa `lab10/guards.py`, thêm chỉ số trong `lab10/monitors.py`.

### Đóng góp cụ thể

- Sửa cổng vòng 2 trong `lab10/guards.py` cho thẻ `S6` (`_resolve_parcel`, đối chiếu kiện–hãng–tài xế trước `file_carrier_fault`, chặn ghi vượt trần 2 lỗi/hãng/ngày, chuyển người duyệt khi đa kiện mơ hồ hoặc lệch quyền lợi).
- Thêm chỉ số theo dõi mới `ambiguous_parcel_rate` trong `lab10/monitors.py`.
- Chạy đánh giá `S6`, kiểm thử hồi quy `base`, dò trace `S6-01`, `S6-20`, `S6-40..43` và tổng hợp C2, C7, C8.

### Bằng chứng

- Commit PR #1 `6c9ce0e` (`feat(gate): vong 2 guards va monitor cho S6`), merge `583a441`.
- `lab10/guards.py`, `lab10/monitors.py`, `templates/form-c-incident.md` (C2, C7, C8), mã chạy `R-S6-grade-20261119-164651-bf477d`.

### Exit ticket

- **Một điều học được:** Với đơn tách kiện, phải đối chiếu ở cấp kiện trước khi ghi. Khi chưa xác định được kiện, chuyển người trước lúc hoàn tiền mới tránh được cả chi sai lẫn quy lỗi oan.
- **Một điều còn chưa chắc:** Trong pilot thật, mã kiện và nguyên nhân trễ có được cập nhật đủ nhanh và đủ chính xác để dùng làm căn cứ tự động không.
- **Ghi nhận dùng AI:** Dùng Codex để hỗ trợ đọc trace, sửa `guards.py` và `monitors.py`, chạy kiểm thử và tổng hợp bằng chứng.

## NguyenHoangGiaAn-2A202603799

### Phần việc phụ trách

Vai **Vận hành và pháp lý**: Câu 1.2 (góc nhìn chị Oanh, chị Hạnh), Câu 1.4 (telemetry production), Câu 2.4 (HAZOP vòng 1 & checklist 9 nhóm có PIC), Câu 2.10 (`operations` & `legal` trong `config/operating_gates.json`, runbook 1–3 & giờ cao điểm), và cuối buổi tổng hợp `submission/submission.json`.

### Đóng góp cụ thể

- Thiết kế telemetry production, HAZOP mở rộng ngoài kỹ thuật, checklist 9 nhóm.
- Cấu hình cổng `operations`, `legal` và viết runbook vận hành vòng 1.

### Bằng chứng

- `config/operating_gates.json`, `templates/form-b-evaluation-gates.md` (mục B4, B5, B7.5, B7.6).

### Exit ticket

- **Một điều học được:** Em đối chiếu `S6-01@11` và thấy lệnh có thể dùng đúng số ngày trễ nhưng vẫn ghi lỗi oan nếu lấy hãng và tài xế của kiện khác. Khi chưa xác định được kiện, chuyển duyệt trước khi ghi giúp tránh cả hoàn sai lẫn quy sai. Report `R-S6-grade-20261119-165504-68b6a6` ghi lỗi hãng oan giảm từ 25 ở prepared xuống 0 ở after.
- **Một điều còn chưa chắc:** Trong pilot thật, tracking có theo kịp việc đổi tài xế sau bàn giao không. Em muốn đối chiếu mẫu với chứng từ hãng và đo thời gian chờ duyệt giờ cao điểm trước Gate 2.
- **Ghi nhận dùng AI:** Em dùng Codex để đọc trace và report, soạn C3.2/C4/C6/C9/C10/C11, cập nhật hai JSON, chạy kiểm thử và chuẩn bị PR #2.
