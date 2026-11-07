# Lab 01 – Câu hỏi thảo luận

## Câu hỏi nhanh: cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?

- `--global` lưu trong `~/.gitconfig` (Windows: `C:\Users\<user>\.gitconfig`), áp dụng cho mọi repository của người dùng.
- `--local` lưu trong `.git/config` của từng repository, chỉ áp dụng cho repository đó và có độ ưu tiên cao hơn `--global`.

## Vì sao dùng `git mv`?

`git mv` di chuyển tệp và ghi nhận thao tác đó vào staging area trong cùng một bước. Git lưu cả thông tin đường dẫn cũ và mới nên vẫn nhận diện được đây là thao tác đổi tên. Nhờ vậy lịch sử của tệp vẫn liền mạch khi dùng `git log --follow`; nếu xóa rồi thêm lại, Git có thể coi là hai tệp khác nhau và làm đứt lịch sử.

## `release/lab01` có phải baseline?

Có. `release/lab01` là trạng thái đã thống nhất dùng để nộp bài. Sau khi tạo, nhánh này đóng băng (chỉ nhận hotfix có kiểm soát), không phát triển tính năng mới trực tiếp trên đó. Đây là baseline của Lab 01 và được đánh dấu bằng tag `v0.1.0` ở Lab 04.

## Vì sao không commit thẳng lên master dù làm một mình?

- Rèn đúng quy trình SCM: mọi thay đổi đi qua nhánh riêng và Pull Request, có mô tả và review.
- Giữ master luôn ở trạng thái ổn định, có thể build/chạy được tại mọi thời điểm.
- Có lịch sử truy vết rõ ràng: yêu cầu → nhánh → commit → PR → merge.
- Khi làm nhóm hoặc bật branch protection, thói quen này giúp tránh việc bị chặn hoặc phá vỡ luồng làm việc.
