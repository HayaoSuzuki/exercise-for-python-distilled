"""0151: 転倒数のリファレンス実装。"""

from collections.abc import Sequence


def count_inversions(seq: Sequence[int]) -> int:
    """seq の転倒数（i < j かつ seq[i] > seq[j] の組の個数）を返す。"""
    a = list(seq)
    buf = list(a)

    def merge_sort(lo: int, hi: int) -> int:
        """a[lo:hi] を昇順に整列し、その範囲内の転倒数を返す。"""
        if hi - lo <= 1:
            return 0
        mid = (lo + hi) // 2
        inversions = merge_sort(lo, mid) + merge_sort(mid, hi)
        i, j = lo, mid
        for k in range(lo, hi):
            if j >= hi or (i < mid and a[i] <= a[j]):
                buf[k] = a[i]
                i += 1
            else:
                buf[k] = a[j]
                j += 1
                inversions += mid - i
        a[lo:hi] = buf[lo:hi]
        return inversions

    return merge_sort(0, len(a))
