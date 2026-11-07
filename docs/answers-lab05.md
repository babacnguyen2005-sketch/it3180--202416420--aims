# Lab 05 – Câu hỏi thảo luận và kiểm toán

## Ưu, nhược điểm của upstream first so với release first

**Upstream first** (sửa trên master trước, sau đó cherry-pick về release):

- Ưu điểm: chỉ có một nguồn sửa lỗi duy nhất; bản sửa luôn có trong phiên bản kế tiếp; ít phân kỳ giữa các dòng.
- Nhược điểm: bản phát hành ổn định phải chờ backport; cherry-pick có thể xung đột nếu mã đã khác; cần kỷ luật lan truyền.

**Release first** (sửa trực tiếp trên release, sau đó đưa về master):

- Ưu điểm: phát hành bản vá nhanh cho người dùng bản ổn định; thay đổi tối thiểu, dễ kiểm thử.
- Nhược điểm: dễ quên lan truyền về master hoặc các release khác; dễ phân kỳ và trùng lặp bản sửa; cần kiểm toán bằng `git cherry`/`git tag --contains`.

## Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào phát hiện?

- `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: chỉ thấy **một** bản cherry-pick thay vì hai.
- `git cherry -v origin/release/lab05 origin/release/lab04`: hiện dấu `+` cho commit sửa lỗi chưa có trên `release/lab05`.
- Vòng lặp kiểm tra hành vi ở Phần F in `0` cho `v1.1.0` (thay vì `1`).
- `git tag --contains <FIX_SHA>` hoặc `git branch --contains <FIX_SHA>` không thấy nhánh/tag tương ứng của dòng 1.1.x.

## Kết quả kiểm toán

```text
$ git log --all --oneline --grep "cherry picked from commit aef1279"
08bb3db fix: make search_by_title case-insensitive
dacc04f fix: make search_by_title case-insensitive

$ git tag --contains aef1279
v1.0.1

$ git cherry -v origin/master origin/release/lab04
- aef1279 fix: make search_by_title case-insensitive
+ d863fed chore: bump version to 1.0.1

$ kiểm tra hành vi trên 3 dòng phiên bản
v1.0.1   1
v1.1.0   1
master   1
```

- `-` nghĩa là master đã có bản tương đương; `+` nghĩa là commit chỉ có trên `release/lab04` (bump phiên bản, đúng chủ đích).
- Bản sửa có mặt trên cả 3 dòng: `v1.0.1`, `v1.1.0`, master.

## Ghi chú môi trường

- Issue #20 và GitHub Release (`v1.0.0`, `v1.1.0`) cần tạo trên giao diện GitHub vì môi trường dòng lệnh không có `gh`/token. Commit đã dùng từ khóa `Fixes #20`/`Refs #20` để liên kết khi Issue tồn tại.
- Branch protection cho `master` và `release/*` cần bật thủ công trong **Settings → Branches**.
- Workflow CI nằm ở `.github/workflows/ci.yml` và chạy trên GitHub Actions cho PR vào master/release và push vào master.
