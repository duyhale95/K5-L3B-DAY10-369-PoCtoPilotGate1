# Kế hoạch phối hợp nhóm · LAB 10 (`K5-L3B-DAY10-369-PoCtoPilotGate1`)

## 1. Phân vai & Sở hữu file (không xung đột Git)

| Thành viên | MSSV | Vai | Nhánh làm việc | File sở hữu (chỉ sửa file của mình) |
|---|---|---|---|---|
| **Hà Lê Duy** | `2A202603851` | Trưởng nhóm · Sản phẩm & Kinh doanh | `main` | `TEAM.md`, `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md` (tổng hợp), `config/acceptance_criteria.json` (đã khóa) |
| **Nguyễn Thiên Bảo** | `2A202603861` | Kỹ sư cổng | `feat/bao-gate-engineer` | `lab10/guards.py`, `lab10/monitors.py` |
| **Nguyễn Hoàng Gia An** | `2A20260379` | Vận hành & Pháp lý | `feat/an-ops-legal` | `config/operating_gates.json`, `submission/submission.json` |

---

## 2. Trạng thái hiện tại: Đã xong CP1 – CP3

- **CP1 (0–15'):** Đã cấu hình Git MSSV, điền `TEAM.md`, chạy `unittest` (`13/13 OK`), lấy `PRD_v1.1.md` & `eval_card.md` từ Lab 9.
- **CP2 (15–65'):** Đã điền Phiếu A & `config/acceptance_criteria.json`, ký (`dd78e606` lúc `2026-11-19T14:24:02`), commit `6e4f816` (`Sign acceptance criteria`) trước khi chạy `eval`.
- **CP3 (65–115'):**
  - Chạy `base` (`R-base-before-20261119-142419-bde05c`), trace `T-002@55`.
  - Code 4 cổng trong `lab10/guards.py` & điền `config/operating_gates.json`.
  - Chạy `lab10.checkpoint` (`3e45ad2b`), `prepared` (`R-base-prepared-20261119-142516-73b283` đạt 5/5 `required` và 3/3 `business_ops`).
  - Điền Phiếu B (B0–B8, quyết định v1: **Tiếp tục**) và push `0540a49` lên `origin main`.

---

## 3. Ai đợi ai & Timeline tiếp theo (CP4 – CP5)

### Giai đoạn chờ (từ nay đến phút 125)
- **Duy:** Mời GitHub Collaborators cho Bảo & An (quyền Write); đợi **BTC** báo số thẻ `S1–S8` và mở repo thẻ.
- **Bảo & An:** Clone repo, tạo nhánh riêng ngay; đọc phần mình đứng tên trong Phiếu A, Phiếu B, `guards.py`, `operating_gates.json` (An điền sẵn `team`, `members`, `decision_v1` trong `submission/submission.json`).

### CP4 · Sự cố & Phiếu C (phút 125–185) — làm song song
1. **Phút 125 (Duy):** Kéo đúng `incidents/Sx` từ repo thẻ, commit và push lên `main`.
2. **Bảo & An:** Cùng chạy `git fetch origin && git merge origin/main` vào nhánh mình.
3. **Làm song song:**
   - **Bảo (`feat/bao-gate-engineer`):** Chạy `grade` mốc `prepared` & `trace` 2 ticket lỗi → sửa `lab10/guards.py` + thêm metric trong `lab10/monitors.py` → chạy `eval` (`Sx` & `base`) + `grade` (`1 integrity ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`) → gửi **C0, C2, C7, C8** cho Duy → **mở PR vào `main`**.
   - **An (`feat/an-ops-legal`):** Đọc `incidents/Sx/card.md`, điền `"incident": "Sx"` trong `submission.json`, soạn **C3, C4, C6** gửi Duy.
   - **Duy (`main`):** Điền **C1, C5** và ghép các phần vào `templates/form-c-incident.md`.
4. **Duy review & merge PR của Bảo vào `main`.**
5. **An:** Pull `main` mới (đã có code của Bảo) → cập nhật `config/operating_gates.json`, chạy `lab10.grade --incident Sx` → soạn **C9, C10, C11** gửi Duy.

### CP5 · Quyết định v2, Demo & Nộp bài (phút 185–240)
1. **Duy:** Chốt **C12** (`decision_v2` & 3 dòng `three_lines`), gửi An điền nốt `submission/submission.json`.
2. **An:** Hoàn tất `submission/submission.json`, push nhánh `feat/an-ops-legal` và **mở PR vào `main`** → **Duy review & merge**.
3. **Cả 3 bạn:** Gửi/cập nhật Exit ticket vào `TEAM.md`; demo ba mốc & phản biện (nếu đổi thử số thì trả về v2 và chạy lại `grade`).
4. **Duy:** Chạy `python -m lab10.check_submission --collect` tới khi ra `ĐỦ THÀNH PHẦN` → push lần cuối lên `main` & gửi link repo cho Lab Coach.
5. **Cả 3 bạn (từng người tự làm):** Nộp link repo lên **LMS** bằng tài khoản cá nhân trước deadline.

---

## 4. Luật cấm chung (tuyệt đối tuân thủ)
- Không sửa `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`, `incidents/Sx/*`.
- Không hardcode theo mã ticket hay câu chữ cụ thể (có test ẩn).
- PR **chỉ** mở vào `duyhale95/K5-L3B-DAY10-369-PoCtoPilotGate1` (`main`), không mở PR về repo mẫu `VinUni-AI20k/...`.
