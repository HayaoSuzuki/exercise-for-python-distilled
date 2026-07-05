"""0653: ハミング数のマージ（Dijkstra の正則数問題）。"""

from __future__ import annotations

import heapq
from collections.abc import Iterator


def hamming() -> Iterator[int]:
    """素因数が 2, 3, 5 のみの正の整数を昇順かつ重複なしで無限に生成する。

    最小ヒープと生成済み集合による実装。ヒープの最小値 x を取り出して
    生成し、2x, 3x, 5x を未登録なら候補として積む。整数演算のみを使う。
    """
    heap = [1]
    seen = {1}
    while True:
        x = heapq.heappop(heap)
        yield x
        for p in (2, 3, 5):
            m = x * p
            if m not in seen:
                seen.add(m)
                heapq.heappush(heap, m)
