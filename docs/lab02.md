# Lab 02 — Feature/topic và PR

- Fetch và merge master trước PR giúp phát hiện conflict, kiểm thử với thay đổi mới, giảm rủi ro lúc tích hợp. Hai nhánh `feature/cart-print` (PR #4) và `feature/search-by-title` (PR #5) được tạo từ cùng baseline; PR #5 được squash nên chỉ còn một commit trên master.
- Không rebase nhánh master/release hoặc nhánh đã chia sẻ khi chưa có đồng thuận: rebase thay SHA, làm lịch sử người khác phân kỳ. Nhánh cá nhân chưa push phù hợp hơn.
- `feature/*` chứa chức năng sản phẩm; `topic/*` dùng cho tài liệu, cấu hình hoặc thay đổi chuyên biệt như `topic/pr-template` (PR #3), `topic/answers-lab02` (PR #6). Đây là quy ước, Git xử lý như nhau.

| Kiểu | SHA/lịch sử | Truy vết và revert |
|---|---|---|
| Merge commit | Giữ SHA commit nguồn, thêm commit hai cha | Giữ cấu trúc nhánh/PR, revert merge bằng `-m 1` |
| Squash | Tạo commit mới chứa tổng diff, không giữ ancestry từng commit nguồn | Dễ revert cả tính năng, lịch sử chi tiết còn trong PR |
| Rebase merge | Viết lại SHA trên đầu nhánh đích, lịch sử thẳng | Từng commit được giữ nội dung; revert theo từng commit, không có merge commit |

- Trước tài liệu này đã có ít nhất 5 thay đổi merged: PR #1 refactor, #2 tài liệu Lab 01, #3 template, #4 cart-print (merge commit), #5 tìm theo tên (squash), #6 tài liệu Lab 02. Nhánh feature dùng merge commit, nhánh search dùng squash.
- Dismiss stale approvals làm approval cũ mất sau push mới để reviewer xem lại thay đổi. Làm một mình nên chưa cấu hình required approval; không tự approve. Branch protection chưa xác minh được qua API công khai (trả 401), cần kiểm tra thủ công.
- Chưa có reviewer thật: chuỗi Request changes → sửa → re-request → Approve chưa thực hiện.
- Use case được thêm ở commit `5d184d5` (PR #5) và tài liệu Lab 02 ở PR #6. Nhật ký: `docs/evidence/lab02.log`.
