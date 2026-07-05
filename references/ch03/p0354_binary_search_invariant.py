"""0354: 不変条件を assert する二分探索 のリファレンス実装。"""


def bisect_left(a: list[int], x: int) -> int:
    """ソート済みリスト a に x を挿入できる最も左の位置を返す。"""
    n = len(a)
    lo, hi = 0, n
    while lo < hi:
        # ループ不変条件
        assert 0 <= lo <= hi <= n
        assert all(a[i] < x for i in range(lo))
        assert all(a[j] >= x for j in range(hi, n))
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    # 事後条件
    assert lo == hi
    assert all(a[i] < x for i in range(lo))
    assert all(a[j] >= x for j in range(lo, n))
    return lo
