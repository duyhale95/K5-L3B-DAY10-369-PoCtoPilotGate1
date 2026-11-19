# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `369`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-369-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): *(chờ phút 125)*

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Hà Lê Duy | 2A202603851 | Sản phẩm và kinh doanh | x |
|   2 | Nguyễn Thiên Bảo | 2A202603861 | Kỹ sư cổng | |
|   3 | Nguyễn Hoàng Gia An | 2A20260379 | Vận hành và pháp lý | |
|   4 | | | | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên:
`["HaLeDuy-2A202603851", "NguyenThienBao-2A202603861", "NguyenHoangGiaAn-2A20260379"]`

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HaLeDuy-2A202603851

### Phần việc phụ trách

Trưởng nhóm · Vai **Sản phẩm và kinh doanh**: lập kế hoạch chia việc 3 thành viên (CP1–CP5), phụ trách Phiếu A (Câu 1.1, 1.5, 1.6), `config/acceptance_criteria.json`, Phiếu B (Câu 2.3 bản đồ dữ liệu & drift, Câu 2.9 `business` trong `config/operating_gates.json`, phần kinh doanh trong B8).

### Đóng góp cụ thể

- Cấu hình repo, bảng thành viên `TEAM.md`, kế hoạch phân công không xung đột file.
- Hoàn thiện Phiếu A và ký `config/acceptance_criteria.json` trước khi chạy đánh giá.
- Hoàn thiện bản đồ dữ liệu, drift và cổng `business` vòng 1.

### Bằng chứng

- Commit `Sign acceptance criteria` và `CP3: ...`
- `templates/form-a-criteria.md`, `config/acceptance_criteria.json`, `templates/form-b-evaluation-gates.md` (mục B3, B7.4).

### Exit ticket

*(Điền cuối buổi trước khi nộp)*

## NguyenThienBao-2A202603861

### Phần việc phụ trách

Vai **Kỹ sư cổng**: Câu 1.3 (offline metric), chạy các lệnh CLI (`eval`, `trace`, `gate`, `checkpoint`, `grade`), Câu 2.1–2.2 (baseline & soát lỗi `T-002@55`), Câu 2.6–2.8 (code cổng vòng 1 trong `lab10/guards.py`, tránh rò rỉ dữ liệu, behavioral test `--adhoc`), và vòng 2 sửa `lab10/guards.py`, thêm chỉ số trong `lab10/monitors.py`.

### Đóng góp cụ thể

- Chạy đánh giá mốc `base`, `after`, `prepared` và ghi nhật ký B0.
- Viết cổng phòng ngừa trong `lab10/guards.py` và kiểm thử `--adhoc`.

### Bằng chứng

- `lab10/guards.py`, `lab10/guards_round1.py`, `templates/form-b-evaluation-gates.md` (mục B0, B1, B2, B7.1–B7.3).

### Exit ticket

*(Điền cuối buổi trước khi nộp)*

## NguyenHoangGiaAn-2A20260379

### Phần việc phụ trách

Vai **Vận hành và pháp lý**: Câu 1.2 (góc nhìn chị Oanh, chị Hạnh), Câu 1.4 (telemetry production), Câu 2.4 (HAZOP vòng 1 & checklist 9 nhóm có PIC), Câu 2.10 (`operations` & `legal` trong `config/operating_gates.json`, runbook 1–3 & giờ cao điểm), và cuối buổi tổng hợp `submission/submission.json`.

### Đóng góp cụ thể

- Thiết kế telemetry production, HAZOP mở rộng ngoài kỹ thuật, checklist 9 nhóm.
- Cấu hình cổng `operations`, `legal` và viết runbook vận hành vòng 1.

### Bằng chứng

- `config/operating_gates.json`, `templates/form-b-evaluation-gates.md` (mục B4, B5, B7.5, B7.6).

### Exit ticket

*(Điền cuối buổi trước khi nộp)*
