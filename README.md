# AIMS-mini — IT3180

MSSV **202416420** · Tài khoản **babacnguyen2005-sketch** · Nhánh chính **master**.

Repository: https://github.com/babacnguyen2005-sketch/it3180--202416420--aims

Ứng dụng Python >= 3.10, chỉ dùng thư viện chuẩn, kiểm thử bằng `unittest`. Đã kiểm chứng bằng Python 3.12.6 local (Windows) và Python 3.12 trên GitHub Actions.

## Cài đặt và chạy

```sh
git clone https://github.com/babacnguyen2005-sketch/it3180--202416420--aims.git
cd it3180--202416420--aims
python -m venv .venv
.venv\Scripts\activate        # Windows; Linux/macOS: source .venv/bin/activate
python main.py
python -m unittest discover -s tests -v
```

Không cần dependency nào ngoài thư viện chuẩn. Demo in `AIMS-mini v1.1.0`, ba DVD và `Total cost: 63.89 $`.

## Chức năng

`DigitalVideoDisc` có title/category/cost. `Cart` giữ tối đa 20 DVD; `add_dvd` trả bool, `total_cost`, `print_cart`, `total_cost_with_discount(percent)` kiểm tra [0,100]. `sort_by_title` và `sort_by_cost` trả danh sách mới đã sắp tăng dần. `search_by_title` tìm chuỗi con không phân biệt hoa thường; `search_by_category` khớp chính xác thể loại (phân biệt hoa thường).

## Xem baseline

| Bài/phiên bản | Nhánh/tag | Kết quả kiểm chứng |
|---|---|---|
| Lab 01 | release/lab01 / v0.1.0 | Demo 63.89; chưa có unittest |
| Lab 02 | release/lab02 / v0.2.0 | Demo, in giỏ, tìm theo tên; chưa có unittest |
| Lab 03 | release/lab03 / v0.3.0 | 3 test PASS |
| Lab 04 baseline | release/lab04 / v1.0.0 | 3 test PASS; chưa sort/category; lỗi tìm "lion" còn tồn tại |
| Bảo trì 1.0.x | v1.0.1 | 5 test PASS; sửa tìm "lion" |
| Lab 05 | release/lab05 / v1.1.0 | 8 test PASS |
| Phát triển | master (1.1.0) | 8 test PASS |

Tag giữ nguyên snapshot; `release/lab04` và `release/lab05` hiện đi trước tag vì có thêm hotfix và tài liệu sau phát hành nên đầu nhánh mới hơn tag. Dùng tag để tái lập bản phát hành:

```sh
git fetch origin --tags
git worktree add --detach ../aims-v1.0.0 v1.0.0
cd ../aims-v1.0.0
python main.py
python -m unittest discover -s tests -v
```

Thay tag để xem baseline khác, dùng đường dẫn worktree mới. Hai baseline Lab 01–02 đều chưa có tests; không xem việc chạy 0 test là PASS kiểm thử chức năng. Lỗi cũ đã nằm trong lịch sử, không sửa lại tag.

## Tài liệu và bằng chứng

- [Câu trả lời Lab 01](docs/lab01.md), [Lab 02](docs/lab02.md), [Lab 03](docs/lab03.md), [Lab 04](docs/lab04.md), [Lab 05](docs/lab05.md).
- [Use case](docs/use-case.md), [CHANGELOG](CHANGELOG.md), [audit hotfix](docs/hotfix-audit.md).
- [Checklist nộp bài](docs/submission-checklist.md), [việc GitHub cần thiếu](docs/github-todo.md), [chỉ mục PR](docs/pull-request-index.md), [log thực tế](docs/evidence/).
- [Issues](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/issues?q=is%3Aissue), [Releases](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/releases), [Actions](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/actions).

## Quy trình đã kiểm chứng

Lịch sử gồm 25 merge commit/PR trên các nhánh `refactor/*`, `feature/*`, `topic/*`, `bugfix/*`, `hotfix/*` cho refactor, tính năng, tài liệu, release và hotfix; mã PR lấy từ commit message và liệt kê ở `docs/pull-request-index.md`. Workflow GitHub Actions chạy unittest với Python 3.12 khi push master và khi có PR vào `master`/`release/**`; hai run CI trên master đã PASS. Issue #1 đã đóng; Releases v1.0.0 và v1.1.0 công khai, v1.0.1 chỉ có tag.

Chưa có partner/reviewer độc lập nên chuỗi Request changes → sửa → re-request → Approve chưa thực hiện; không tự approve. Branch protection chưa xác minh được qua API công khai (trả 401), cần kiểm tra thủ công trong Settings → Branches. Repository hiện trả 0 pull request object qua API; lịch sử được đẩy lên dưới dạng merge commit, xem chi tiết ở `docs/github-todo.md`.
