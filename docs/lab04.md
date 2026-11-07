# Lab 04 — Release flow và baseline

- SemVer MAJOR.MINOR.PATCH: tăng MAJOR khi thay API không tương thích; MINOR khi thêm tính năng tương thích; PATCH khi sửa lỗi tương thích. Với `0.y.z` API chưa ổn định (Lab 01–03 dùng `v0.1.0`…`v0.3.0`). Bài chọn `1.0.0` để đánh dấu baseline chức năng ổn định, không phải cứ Lab 04 là phải thành `0.4.0`.
- Tag là tên trỏ commit; annotated tag thêm metadata/message và không di chuyển tag đã công bố. Release branch là ref có thể tiến qua các PR bảo trì. GitHub Release là mô tả và asset gắn tag, khác cả hai.
- Chuẩn bị version, CHANGELOG và tài liệu trên master qua PR #14 (`3b7686a`) trước, rồi tạo `release/lab04` từ master và tag `v1.0.0` tại `60528c4` để baseline có đủ nội dung đã kiểm tra.
- Không merge `release/*` ngược master vì có commit version và thay đổi bảo trì riêng dòng; chuyển commit fix cần thiết bằng `cherry-pick -x` qua PR.
- `git log A..B` liệt kê commit reachable từ B nhưng không reachable từ A. `git diff A B` so nội dung snapshot hai đầu, không liệt kê tập commit. Trước hotfix, `master..release/lab04` rỗng; `release/lab04..master` có các commit phát triển tiếp.
- Detached HEAD nghĩa là HEAD trỏ trực tiếp commit, không bám nhánh; commit mới có thể mất tên tham chiếu nếu không tạo branch. Worktree là working directory bổ sung chia sẻ object database; có thể checkout branch hoặc detached HEAD. Dùng `git worktree add --detach <path> v1.0.0` để kiểm tra baseline mà không đổi working tree chính.
- Bốn annotated tag được tạo sau khi baseline đã chốt: `v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`. Không di chuyển tag.
- Audit worktree chạy `main.py`, `unittest`, kiểm tra version/file/CHANGELOG, `git archive`. Vì bằng chứng phát sinh sau baseline, được bổ sung bằng PR tiếp theo (PR #16) trước hotfix, không sửa tag/baseline để đưa log vào.

## Kiểm toán cấu hình v1.0.0

```text
$ git show v1.0.0:aims/__init__.py
__version__ = "1.0.0"

$ git diff --stat v0.3.0 v1.0.0
 CHANGELOG.md     | 21 +++++++++++++++++++++
 aims/__init__.py |  2 +-
 main.py          |  2 ++
 3 files changed, 24 insertions(+), 1 deletion(-)

$ git ls-tree -r --name-only v1.0.0
.gitattributes
.github/pull_request_template.md
.gitignore
CHANGELOG.md
README.md
aims/__init__.py
aims/cart.py
aims/dvd.py
aims/search.py
docs/answers-lab01.md   (đổi tên thành docs/lab01.md ở working tree)
docs/answers-lab02.md   (đổi tên thành docs/lab02.md ở working tree)
docs/answers-lab03.md   (đổi tên thành docs/lab03.md ở working tree)
docs/use-case.md
main.py
tests/test_cart.py
tests/test_discount.py

$ python main.py
Total cost: 63.89 $

$ python -m unittest discover -s tests -v
Ran 3 tests in 0.00s
OK

$ git describe --tags --exact-match v1.0.0
v1.0.0

$ git archive --format=tar.gz --prefix=aims-mini-1.0.0/ --output=aims-mini-1.0.0.tar.gz v1.0.0
```

- Trên master có `sort_by_title`/`sort_by_cost` và `search_by_category`; trên `release/lab04` (tại tag `v1.0.0`) không có, đúng chủ đích đóng băng baseline.

## GitHub Release

Hai release công khai đã tạo trên giao diện GitHub: `v1.0.0` và `v1.1.0`. `v1.0.1` chỉ có annotated tag, chưa có release object. Môi trường dòng lệnh không có `gh`/token nên thao tác release được thực hiện thủ công; xem `docs/evidence/lab04.log`.
