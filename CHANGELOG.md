# Changelog

Mọi thay đổi đáng chú ý của dự án được ghi lại trong tệp này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/vi/1.1.0/) và dự án tuân theo [Semantic Versioning](https://semver.org/lang/vi/).

## [Unreleased]

## [1.0.0] - 2026-11-07

### Added

- `Cart.print_cart()` in giỏ hàng và tổng tiền.
- `search_by_title()` tìm đĩa theo tựa đề.
- `Cart.total_cost_with_discount()` tính tổng tiền sau giảm giá.
- Pull request template và tài liệu use-case.

### Fixed

- Giỏ hàng từ chối đĩa thứ 21 trở đi (`MAX_NUMBERS_ORDERED`).
- Công thức giảm giá trả đúng số tiền sau giảm và kiểm tra phần trăm hợp lệ.
