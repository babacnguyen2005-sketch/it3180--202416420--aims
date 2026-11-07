# Lab 05 — Hotfix và bảo trì nhiều phiên bản

- Hotfix tạo từ `release/lab04` để chỉ sửa nền 1.0.x; tạo từ master sẽ lẫn sort/category của dòng 1.1.0. Không merge release ngược master.
- Commit sửa search và regression test tách khỏi commit version/CHANGELOG để cherry-pick đúng patch lên các dòng khác, không hạ version master xuống 1.0.1. FIX_SHA: `aef127930999fd911bbc370e76b6d4aa179185b9`.
- `git cherry-pick -x FIX_SHA` tạo commit mới, ghi nguồn patch trong message. Merge toàn hotfix có thể mang version/changelog của dòng cũ và quan hệ lịch sử không mong muốn.
- Nếu `v1.1.0` đã công bố thì sửa lỗi bằng `v1.1.1`; không đổi tag `v1.1.0`. Trong bài, `release/lab05` chưa gắn tag tại thời điểm hotfix nên có thể đưa fix qua PR #21 trước tag `v1.1.0`.
- Release-first: sửa ở dòng phát hành bị ảnh hưởng rồi forward-port lên master/dòng mới. Upstream-first: sửa master rồi backport dòng cũ. Chọn theo nguồn lỗi, phụ thuộc và mức khẩn cấp; cả hai cần ma trận phiên bản và regression test.
- Phát hiện sót patch trên `release/lab05` bằng tìm nguồn cherry-pick trong log, so patch bằng `git cherry`, và chạy test tìm “lion” trên từng worktree. Cần kiểm tra cả hành vi và version.
- `git cherry -v master release/lab04`: dấu `-` là patch có tương đương trên upstream; `+` chưa có patch tương đương (ví dụ commit version `d863fed`). Với commit merge, patch-id không đủ thay thế audit nội dung.
- `git tag --contains FIX_SHA` chỉ xét ancestry: tag chứa commit nguồn; tag có cherry-pick tương đương nhưng SHA khác có thể không xuất hiện. Kết quả: `v1.0.1`.
- GitHub Actions dùng Python 3.12, chạy unittest cho push master; workflow cho PR vào `master`/`release/**` đã cấu hình nhưng repository hiện có 0 pull request object nên chưa có run do PR. Hai run CI trên master đều PASS.

## Kết quả kiểm toán

```text
$ git log --all --oneline --grep "cherry picked from commit aef1279"
08bb3db fix: make search_by_title case-insensitive
dacc04f fix: make search_by_title case-insensitive

$ git tag --contains aef1279
v1.0.1

$ git cherry -v master release/lab04
- aef1279 fix: make search_by_title case-insensitive
+ d863fed chore: bump version to 1.0.1
- 6d13b85 docs: answer lab04 discussion questions and audit

$ ma trận hành vi tìm "lion"
v1.0.0   []                 version 1.0.0, 3 test
v1.0.1   ['The Lion King']  version 1.0.1, 5 test
v1.1.0   ['The Lion King']  version 1.1.0, 8 test
master   ['The Lion King']  version 1.1.0, 8 test
```

- `-` nghĩa là đã có bản tương đương trên upstream; `+` là commit chỉ có trên `release/lab04` (bump phiên bản, đúng chủ đích).
- Bản sửa có mặt trên cả ba dòng `v1.0.1`, `v1.1.0`, master, nhưng master giữ version 1.1.0.

## Ghi chú môi trường

- Issue #1 (search_by_title case-sensitive) đã đóng. Release `v1.0.0`/`v1.1.0` tạo trên giao diện GitHub; `v1.0.1` chỉ có tag.
- Branch protection cho `master` và `release/*` chưa xác minh được qua API công khai (401); cần bật/kiểm tra thủ công trong Settings → Branches.
- Workflow CI ở `.github/workflows/ci.yml`; log: `docs/evidence/lab05-ci.log`, `docs/evidence/lab05-hotfix.log`.
