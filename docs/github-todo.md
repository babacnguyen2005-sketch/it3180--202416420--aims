# GitHub — việc còn thiếu và trạng thái

- Repository công khai: https://github.com/babacnguyen2005-sketch/it3180--202416420--aims. GitHub đặt default branch là `main`; `master` đang cùng commit `9b440dc`.
- Đã làm: Issue [#1](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/issues/1) (search_by_title case-sensitive) đã đóng; các nhánh `release/lab01`…`release/lab05` và tag `v0.1.0`…`v1.1.0` đã push; Releases [v1.0.0](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/releases/tag/v1.0.0) và [v1.1.0](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/releases/tag/v1.1.0); CI push master chạy 2 lần đều PASS.
- Lịch sử local có 25 merge commit mang mã PR #1–#25 (`docs/pull-request-index.md`), nhưng API công khai của repository hiện trả **0 pull request object**. Nếu môn học yêu cầu PR thật, cần mở lại PR từ các nhánh nguồn hoặc nộp kèm chỉ mục merge commit này.
- **Chưa làm**: review độc lập Request changes → sửa → re-request → Approve. Chưa có partner được chỉ định, không tự approve. Khi có partner, yêu cầu review trên PR mới và tăng required approval từ 0 lên 1 theo quy định nhóm.
- **Chưa xác minh**: branch protection cho `master` và `release/*`, required check `unit-tests`. API công khai trả 401 Unauthorized nên không đọc được cấu hình; cần kiểm tra thủ công trong Settings → Branches.
- **Chưa làm**: GitHub Release cho `v1.0.1`. Tag `v1.0.1` đã có và đã push; chỉ thiếu release object.
- CI đã cấu hình cho push `master` và PR vào `master`/`release/**`; do repository hiện không có PR object nên mới có run do push master.
- Snapshot tài liệu này được chụp trước commit/PR báo cáo cuối; xem danh sách commit trực tiếp để có trạng thái mới nhất.
