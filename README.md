# AIMS-mini

Bài thực hành IT3180 – Quản lý cấu hình phần mềm với Git & GitHub.

Ứng dụng dòng lệnh Python quản lý giỏ hàng DVD, chỉ dùng thư viện chuẩn và kiểm thử bằng `unittest`.

## Yêu cầu

- Git >= 2.40
- Python >= 3.10 (chỉ dùng thư viện chuẩn)

## Cấu trúc dự án

```
.github/          PR template, GitHub Actions workflow
aims/             mã nguồn package (cart, dvd, search)
docs/             tài liệu use-case và câu trả lời thảo luận
tests/            kiểm thử unittest
CHANGELOG.md      lịch sử phiên bản
main.py           chương trình demo
```

## Chạy chương trình

```bash
python main.py
```

Kết quả mong đợi: `Total cost: 63.89 $`.

## Chạy kiểm thử

```bash
python -m unittest discover -s tests -v
```

## Quy trình Release Flow

| Nhánh | Tạo từ | Merge vào | Mục đích |
| --- | --- | --- | --- |
| feature/<tên>, topic/<mô-tả> | master | master | Tính năng / chủ đề |
| bugfix/<mô-tả> | master / feature | master / feature | Sửa lỗi khi phát triển |
| refactor/<mô-tả> | master / feature | master / feature | Tái cấu trúc |
| release/labXX | master | không | Nộp bài |
| hotfix/<mô-tả> | release | release & master | Sửa bài đã nộp |

Không commit trực tiếp lên master và release/*. Mọi thay đổi đi qua Pull Request.
