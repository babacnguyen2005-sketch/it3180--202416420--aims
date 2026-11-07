# Changelog

Theo Keep a Changelog; phiên bản tuân theo SemVer. Ngày theo Asia/Ho_Chi_Minh.

## [Unreleased]

## [1.1.0] - 2026-11-07

### Fixed
- Đã tích hợp bản vá tìm tên không phân biệt hoa thường của 1.0.1 vào dòng 1.1.0.

### Added
- Tìm kiếm theo thể loại khớp chính xác thể loại.
- Sắp xếp giỏ tăng dần theo tên hoặc giá, trả danh sách mới.

## [1.0.1] - 2026-11-07

### Fixed
- `search_by_title()` tìm tên không phân biệt hoa thường (forward-port bản vá 1.0.x).

## [1.0.0] - 2026-11-07

### Added
- Mô hình DVD, giỏ hàng, thêm DVD, tính tổng và hiển thị giỏ.
- Tìm kiếm theo tên (phân biệt hoa thường ở baseline này).
- Tính tổng sau giảm giá với kiểm tra phần trăm 0–100.
- Đóng gói `aims`, sơ đồ use case, tài liệu và kiểm thử unittest.

### Fixed
- Từ chối DVD thứ 21, giữ giới hạn 20 DVD.
- Công thức giảm giá trả đúng số tiền còn lại, kiểm tra phần trăm ngoài giới hạn.
- Kết hợp xung đột thông báo thêm DVD, sau đó revert phần hiển thị tên DVD để thực hành; giữ thông báo tiếng Việt.
