"""0603: オンライン分散のコルーチン（Welford 法）。"""

from __future__ import annotations

from collections.abc import Generator

Result = tuple[int, float, float]


def stats() -> Generator[Result | None, float]:
    """send(x) で値を受け取るたびに（個数, 平均, 母分散）を返す拡張ジェネレータ。

    Welford 法により、個数 n、平均 mean、偏差積和 m2 の3変数だけを
    O(1) メモリで更新する。母分散は m2 / n。
    """
    n = 0
    mean = 0.0
    m2 = 0.0
    result: Result | None = None
    while True:
        x = yield result
        n += 1
        delta = x - mean
        mean += delta / n
        m2 += delta * (x - mean)
        result = (n, mean, m2 / n)
