# Lab 01 — Thiết lập và refactor

MSSV: 202416420. Ngày thực hiện: 2026-11-07 (Asia/Ho_Chi_Minh).

- Working directory là các file đang làm việc; staging area (index) giữ nội dung dự kiến cho commit tiếp theo; local repository (.git) lưu object, commit và refs.
- `git config --global` thường lưu ở `~/.gitconfig` (Windows: `%USERPROFILE%\.gitconfig`) hoặc `$XDG_CONFIG_HOME/git/config`, áp dụng cho mọi repository của người dùng. `--local` lưu `.git/config`, chỉ áp dụng repository hiện tại và có độ ưu tiên cao hơn global. Bài này chỉ cấu hình local.
- `git mv` chuyển file và stage việc chuyển trong cùng một bước. Git lưu snapshot và nhận diện rename bằng độ giống nhau khi diff/log, không lưu một object rename riêng. Commit chuyển file độc lập giúp xem xét rõ ràng; `git log --follow -- aims/cart.py` theo lịch sử trước rename.
- Nhánh `refactor/apply-release-flow` tách từ master, đổi cấu trúc sang package `aims/` (commit `88d073c`, `03b90b3`) rồi merge qua PR #1 (`1a8ee55`). Tài liệu Lab 01 vào bằng PR #2 (`395e224`). `release/lab01` được tạo từ master sau hai PR này và gắn tag `v0.1.0`, làm baseline để đối chiếu; sửa đổi sau phải qua PR, không chỉnh baseline để thêm bằng chứng.
- Làm một mình vẫn dùng nhánh riêng và merge commit/PR để xem diff, kiểm thử, ghi lý do và giữ dấu tích hợp. Không có partner nên chưa thực hiện review độc lập hay approval.

## Hoàn tác thực tế

Thực hành trên bản clone tạm nên không đụng lịch sử công bố. Đã thêm dòng TEMP vào README rồi `git restore README.md`, diff trở về sạch. Đã stage `docs/amend-practice.txt`, `git restore --staged` để đưa khỏi index nhưng giữ working file. Đã commit tạm `78c4a48`, `git commit --amend -m ...` trên commit chưa push thành `d9305f4`, sau đó xóa file tạm bằng commit riêng. Nhật ký: `docs/evidence/lab01.log`.

## Kiểm chứng

Mã ban đầu ở thư mục gốc chạy bằng Python 3.12 in tổng `63.89 $`. Refactor dùng package `aims`, commit chuyển file và sửa import riêng; chạy lại vẫn cùng tổng. Baseline `release/lab01` / `v0.1.0` chưa có unittest (0 test). Lỗi giới hạn giỏ — nhận DVD thứ 21 — được cố ý giữ đến Lab 03.
