# AIMS-mini – Use case

## Tác nhân

- **Khách hàng**: người dùng thêm đĩa vào giỏ, xem giỏ, tìm kiếm và sắp xếp.
- **Quản trị viên**: người cập nhật danh mục đĩa (mở rộng trong tương lai).

## Use case

| Mã | Use case | Tác nhân | Mô tả |
| --- | --- | --- | --- |
| UC01 | Thêm đĩa vào giỏ | Khách hàng | Thêm một DVD, giỏ tối đa 20 đĩa |
| UC02 | Xem giỏ hàng | Khách hàng | In danh sách đĩa và tổng tiền |
| UC03 | Tính tổng tiền | Khách hàng | Tính tổng giá của các đĩa trong giỏ |
| UC04 | Tìm theo tựa đề | Khách hàng | Tìm các đĩa có tựa chứa từ khóa |
| UC05 | Tìm theo thể loại | Khách hàng | Tìm các đĩa thuộc một thể loại |
| UC06 | Sắp xếp giỏ hàng | Khách hàng | Sắp xếp theo tựa đề hoặc theo giá |
| UC07 | Áp dụng giảm giá | Khách hàng | Tính tổng tiền sau khi giảm theo phần trăm |

## Sơ đồ

```text
            +------------------+
            |    Khách hàng    |
            +------------------+
                     |
     +---------------+----------------+
     |               |                |
 (UC01)          (UC02, UC03)     (UC04, UC05)
 Thêm đĩa         Xem giỏ /        Tìm kiếm
                  tính tiền
     |               |                |
     +---------------+----------------+
                     |
              (UC06, UC07)
         Sắp xếp / áp dụng giảm giá
```
