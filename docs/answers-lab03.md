# Lab 03 – Câu hỏi thảo luận

## Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh, tức điểm mà hai nhánh tách ra. Git dùng merge base làm mốc thứ ba trong 3-way merge (base, nhánh hiện tại, nhánh cần merge) để tính ra thay đổi của mỗi bên và kết hợp chúng. Có thể xem bằng `git merge-base <nhánh-A> <nhánh-B>`.

## Vì sao master và release/* phải dùng revert?

- `master` và `release/*` là lịch sử đã chia sẻ, người khác có thể đã pull hoặc dựa vào commit SHA.
- `reset` và `rebase` viết lại lịch sử, tạo SHA mới, có thể làm hỏng lịch sử chung và buộc người khác phải xử lý lại.
- `revert` tạo một commit mới đảo ngược thay đổi, giữ nguyên lịch sử cũ, an toàn để push và vẫn truy vết được.
- Với merge commit, cần `git revert -m 1 <sha>` để chọn nhánh first-parent làm trạng thái cần quay về.

Quy tắc: chỉ dùng `reset`/`rebase`/`amend` trên commit chưa push; commit đã chia sẻ thì dùng `revert`.
