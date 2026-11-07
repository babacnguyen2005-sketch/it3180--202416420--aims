# Lab 02 – Câu hỏi thảo luận

## Vì sao phải đồng bộ master trước khi gửi PR?

- Phát hiện sớm xung đột tích hợp khi master đã đi trước, thay vì để đến lúc merge mới xử lý.
- Đảm bảo PR được kiểm thử trên mã mới nhất, tránh trường hợp test xanh trên nhánh cũ nhưng đỏ sau khi merge.
- Reviewer thấy đúng phần thay đổi so với master hiện tại, giảm diff nhiễu.
- Giữ nhánh sống ngắn, gần master, tránh "merge hell".

## Khi nào không được rebase?

- Không rebase commit đã chia sẻ (đã push lên master, release/* hoặc nhánh của người khác) vì rebase viết lại lịch sử, tạo SHA mới và làm rối lịch sử chung.
- Không rebase nhánh đang được review nếu chưa thống nhất với reviewer, vì approval có thể bị vô hiệu và diff thay đổi ngoài dự kiến.
- Với nhánh riêng chưa chia sẻ hoặc vừa đồng bộ master thì có thể rebase; nếu đã push thì dùng `--force-with-lease` và chỉ khi chắc chắn không ai dựa vào nhánh đó.

## `feature/*` khác `topic/*` như thế nào?

Cả hai đều là nhánh sống ngắn, tạo từ master và merge trở lại master qua Pull Request. Trong học phần:

- `feature/*` dùng cho tính năng/code có ý nghĩa sản phẩm, thường gắn với Issue và có test.
- `topic/*` dùng cho thay đổi nhỏ hoặc chủ đề tài liệu, cấu hình, template (ví dụ `topic/pr-template`, `topic/use-case-diagram`).

Điểm khác biệt chủ yếu là quy ước đặt tên và phạm vi thay đổi; quy trình kiểm soát thay đổi là như nhau.
