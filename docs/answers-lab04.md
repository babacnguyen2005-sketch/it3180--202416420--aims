# Lab 04 – Câu hỏi thảo luận và kiểm toán

## Vì sao `release/*` không merge ngược vào master?

- `release/*` là dòng bảo trì của một baseline đã phát hành, chỉ nhận hotfix; master là dòng phát triển tiếp.
- Merge `release/*` vào master sẽ mang theo các commit chỉ thuộc bản phát hành (bump phiên bản, changelog, hotfix) và có thể gây xung đột với phiên bản mới hơn trên master.
- Cách đúng là sửa lỗi trên nhánh hotfix rồi lan truyền bằng `cherry-pick` sang cả `release/*` và master (xem Lab 05), nhờ vậy mỗi dòng giữ lịch sử riêng và có thể kiểm toán.

## So sánh với GitFlow

| Điểm | Release Flow (học phần) | GitFlow |
| --- | --- | --- |
| Nhánh chính | master | main và develop |
| Nhánh release | Tạo từ master, không merge ngược | Tạo từ develop, merge vào main và develop |
| Hotfix | Tạo từ release/*, đưa về release/* và master | Tạo từ main, đưa về main và develop |
| Phù hợp | Nộp bài theo tuần, nhiều bản song song | Phát hành định kỳ, nhiều môi trường |

## Vì sao lên 1.0.0 mà không phải 0.4.0?

- `0.y.z` là giai đoạn phát triển ban đầu, API chưa ổn định (Lab 01–03 dùng `v0.1.0`…`v0.3.0`).
- Lab 04 đánh dấu baseline ổn định đầu tiên được phát hành chính thức: API đã đủ dùng, có CHANGELOG, tag và quy trình bảo trì.
- Theo SemVer, mốc `1.0.0` biểu thị sản phẩm đã đạt phiên bản ổn định; `0.4.0` chỉ là một bước tiền phát hành nữa, không phản ánh việc chuyển sang giai đoạn ổn định.

## Status accounting

```text
$ git log --oneline release/lab04..master
b503338 Merge pull request #15 from babacnguyen2005-sketch/feature/sort-cart
0cd709c feat: add sort_by_title and sort_by_cost to Cart

$ git log --oneline master..release/lab04
(không có kết quả – release/lab04 không có commit nào ngoài master)

$ git diff --stat v0.3.0 v1.0.0
 CHANGELOG.md     | 21 +++++++++++++++++++++
 aims/__init__.py |  2 +-
 main.py          |  2 ++
 3 files changed, 24 insertions(+), 1 deletion(-)

$ git diff --stat v1.0.0 master
 CHANGELOG.md       |  4 ++++
 aims/cart.py       |  6 ++++++
 tests/test_sort.py | 24 ++++++++++++++++++++++++
 3 files changed, 34 insertions(+)

$ git describe --tags
v1.0.0-2-gb503338

$ git log --oneline --no-merges v0.3.0..v1.0.0
3b7686a chore: prepare release 1.0.0
```

## Kiểm toán cấu hình v1.0.0

- `git show v1.0.0:aims/__init__.py` → `__version__ = "1.0.0"`.
- `git ls-tree -r --name-only v1.0.0` không có tệp rác (`__pycache__`, `.venv`, ...).
- Worktree `v1.0.0`: chạy 3 test, tất cả OK.
- `git archive` tạo được gói `aims-1.0.0.zip` từ tag.
- Trên master có `sort_by_title`/`sort_by_cost`; trên `release/lab04` không có (đúng chủ đích đóng băng baseline).

## GitHub Release

Do môi trường dòng lệnh không có `gh`/token nên GitHub Release được tạo thủ công:

1. Vào **Releases → Draft a new release**.
2. Chọn tag có sẵn `v1.0.0`, target `release/lab04`.
3. Tiêu đề: `AIMS-mini 1.0.0`.
4. Dán nội dung mục `[1.0.0]` trong `CHANGELOG.md`.
5. Publish.
