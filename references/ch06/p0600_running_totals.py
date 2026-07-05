"""0600: 累積和ジェネレータのリファレンス実装。"""

from collections.abc import Iterable, Iterator


def running_totals(values: Iterable[int]) -> Iterator[int]:
    """入力の累積和を順に生成する。"""
    total = 0
    for value in values:
        total += value
        yield total
