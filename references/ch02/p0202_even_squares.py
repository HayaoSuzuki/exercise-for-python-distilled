"""0202: 偶数だけの平方のリファレンス実装。"""

from collections.abc import Iterable


def even_squares(values: Iterable[int]) -> list[int]:
    """values に含まれる偶数だけを平方して返す。"""
    return [value * value for value in values if value % 2 == 0]
