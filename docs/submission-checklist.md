# Checklist nộp bài IT3180 — 202416420

Ngày thực hiện: 2026-11-07, Asia/Ho_Chi_Minh. Các link là kết quả GitHub thực tế; log không giả lập.

| Hạng mục | Trạng thái | Bằng chứng |
|---|---|---|
| Kiểm tra môi trường, danh tính local, root commit | Đã làm | `evidence/final-audit.log`; commit `f92412c`, `76bdb5b` |
| Lab 01: khởi tạo, mã gốc, restore/staged/amend, refactor, PR, release | Đã làm | `lab01.md`; merge #1–#2; `evidence/lab01.log` |
| Lab 02: template, hai nhánh cùng baseline, 3 kiểu merge, use case, ≥5 PR | Đã làm | merge #1–#6; `lab02.md`; `evidence/lab02.log` |
| Lab 03: Issue, test FAIL/PASS, sửa lỗi giới hạn, discount PR vào feature | Đã làm | Issue #1; merge #7–#9; `lab03-limit-*.log` |
| Conflict thật, giải quyết kết hợp, revert merge `-m 1` | Đã làm | merge #10–#12; `evidence/lab03.log`; `lab03.md` |
| Reset soft/mixed/hard riêng, reflog và rescue | Đã làm (bản clone tạm) | `evidence/lab03.log`; nhánh `rescue/reset-demo` |
| Lab 04: chuẩn bị version/tài liệu trước baseline, annotated tags, release | Đã làm | merge #14; Releases v1.0.0/v1.1.0; `evidence/lab04.log` |
| Sort sau baseline, audit trước hotfix, worktree/archive 1.0.0 | Đã làm | merge #15–#16; `evidence/lab04.log` |
| Lab 05: category, version 1.1.0/tài liệu trước release/lab05 | Đã làm | merge #17–#18; `lab05.md` |
| Hotfix từ release/lab04, FIX_SHA, tách commit version | Đã làm | merge #19; `hotfix-audit.md` |
| Diff v1.0.0..v1.0.1 đúng bốn file, không sort/category | Đã làm | `evidence/lab05-hotfix.log` |
| Cherry-pick `-x` đúng FIX_SHA lên master/lab05, không hạ version | Đã làm | merge #20–#21; log grep/cherry/tag `--contains` |
| Issue đã đóng | Đã làm | Issue #1 `CLOSED` |
| Ma trận v1.0.0/v1.0.1/v1.1.0/master | Đã làm | 3/5/8/8 test PASS; `evidence/lab05-hotfix.log` |
| Bảo vệ master/release/*, required check | Chưa xác minh | API công khai trả 401; cần kiểm tra Settings → Branches |
| CI Python 3.12, PR master/release/**, push master | Đã làm một phần | `.github/workflows/ci.yml`; 2 run push master PASS; chưa có run do PR vì repo hiện 0 PR object |
| Review độc lập Request changes → sửa → re-request → Approve | Chưa làm | Chưa có partner; không tự approve |
| GitHub Release v1.0.1 | Chưa làm | Chỉ có annotated tag `v1.0.1` |
| README, 5 answers, checklist, log | Đã làm (working tree) | PR/commit tiếp theo |

Snapshot có 25 merge commit/PR trước tài liệu này. Repository công khai hiện trả 0 pull request object qua API; lịch sử được đẩy lên dưới dạng merge commit, xem `github-todo.md`. Không tuyên bố hoàn thành review độc lập hay branch protection. Người dùng cần chỉ định partner nếu môn học bắt buộc chu trình review thật.
