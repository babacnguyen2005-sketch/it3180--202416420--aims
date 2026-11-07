# Chỉ mục PR / merge commit

Snapshot từ lịch sử Git. Repository công khai hiện trả 0 pull request object qua API, nên mỗi dòng liên kết tới merge commit thật; mã PR lấy từ commit message của merge commit.

| PR | Nội dung | Base | Trạng thái | Commit |
|---|---|---|---|---|
| #1 | refactor: chuyển mã nguồn vào package `aims` | master | MERGED | [`1a8ee55`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/1a8ee55) |
| #2 | docs: trả lời câu hỏi Lab 01 | master | MERGED | [`395e224`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/395e224) |
| #3 | docs: thêm template pull request | master | MERGED | [`aa425ae`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/aa425ae) |
| #4 | feat: in giỏ hàng và tổng tiền | master | MERGED | [`2120b22`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/2120b22) |
| #5 | feat: tìm DVD theo tên (squash) | master | MERGED | [`972e038`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/972e038) |
| #6 | docs: trả lời câu hỏi Lab 02 và use case | master | MERGED | [`4d39597`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/4d39597) |
| #7 | fix: chặn DVD thứ 21 (lỗi giới hạn giỏ) | master | MERGED | [`f477164`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/f477164) |
| #8 | fix: trả đúng tổng sau giảm giá và kiểm tra phần trăm | feature/discount | MERGED | [`0bd9c8b`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/0bd9c8b) |
| #9 | feat: thêm `total_cost_with_discount` | master | MERGED | [`dcfc0d9`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/dcfc0d9) |
| #10 | feat: thông báo tiếng Việt khi thêm DVD | master | MERGED | [`de9850a`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/de9850a) |
| #11 | feat: hiển thị tên DVD trong thông báo | master | MERGED | [`2c17e39`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/2c17e39) |
| #12 | fix: revert merge hiển thị tên DVD (thực hành) | master | MERGED | [`a60c465`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/a60c465) |
| #13 | docs: trả lời câu hỏi Lab 03 | master | MERGED | [`74e7433`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/74e7433) |
| #14 | chore: chuẩn bị baseline 1.0.0 | master | MERGED | [`60528c4`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/60528c4) |
| #15 | feat: sắp xếp giỏ hàng theo tên/giá | master | MERGED | [`b503338`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/b503338) |
| #16 | docs: trả lời Lab 04 và audit baseline | master | MERGED | [`1324828`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/1324828) |
| #17 | feat: tìm DVD theo thể loại | master | MERGED | [`ce10aa9`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/ce10aa9) |
| #18 | chore: chuẩn bị release 1.1.0 | master | MERGED | [`ad1f1ec`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/ad1f1ec) |
| #19 | fix: tìm kiếm không phân biệt hoa thường cho dòng 1.0.x | release/lab04 | MERGED | [`b119564`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/b119564) |
| #20 | fix: chuyển bản vá tìm kiếm lên master | master | MERGED | [`f60deb7`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/f60deb7) |
| #21 | fix: chuyển bản vá tìm kiếm sang release/lab05 | release/lab05 | MERGED | [`4bac522`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/4bac522) |
| #22 | ci: thêm workflow unittest | master | MERGED | [`64383c2`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/64383c2) |
| #23 | docs: trả lời Lab 05 và audit hotfix | master | MERGED | [`9b440dc`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/9b440dc) |
| #24 | docs: bổ sung tài liệu Lab 05 cho release/lab05 | release/lab05 | MERGED | [`df3e8e5`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/df3e8e5) |
| #25 | docs: bổ sung tài liệu Lab 04 cho release/lab04 | release/lab04 | MERGED | [`4dfbbb7`](https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/commit/4dfbbb7) |

PR #5 là squash nên không có merge commit hai cha; các PR còn lại là merge commit. Toàn bộ nhánh nguồn đã được đẩy lên remote và có thể xem lại bằng `git log --merges`.
