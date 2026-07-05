"""0300: 最初の重複値のリファレンス実装。"""

from collections.abc import Iterable


def first_duplicate(values: Iterable[int]) -> int | None:
    """2回目の出現位置が最も左にある値を返す。"""
    seen: set[int] = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None
