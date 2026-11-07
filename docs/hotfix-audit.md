# Audit hotfix

FIX_SHA: `aef127930999fd911bbc370e76b6d4aa179185b9`

Issue: https://github.com/babacnguyen2005-sketch/it3180--202416420--aims/issues/1

Commit fix chỉ chứa `aims/search.py` và `tests/test_search.py`; commit kế tiếp (`d863fed`) chứa version và CHANGELOG. Diff `v1.0.0` → `v1.0.1` dùng 4 file. Cherry-pick `-x` lên master (`dacc04f`) và `release/lab05` (`08bb3db`), không merge release ngược master. Master giữ version 1.1.0.

| Ref | Version | Tìm "lion" | Sort/category |
|---|---|---|---|
| v1.0.0 | 1.0.0 | [] (lỗi tái hiện) | Không |
| v1.0.1 | 1.0.1 | The Lion King | Không |
| v1.1.0 | 1.1.0 | The Lion King | Có |
| master | 1.1.0 | The Lion King | Có |

Kết quả unittest, ancestry tags, patch equivalence và log: `docs/evidence/lab05-hotfix.log`. `git tag --contains` không thể dùng thay kiểm tra patch cherry-picked.
