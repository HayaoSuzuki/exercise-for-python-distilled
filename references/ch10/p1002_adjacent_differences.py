"""1002: zip で作る隣接差のリファレンス実装。"""

from collections.abc import Sequence


def adjacent_differences(values: Sequence[int]) -> list[int]:
    """隣り合う値について、後ろの値から前の値を引いた差を返す。"""
    return [right - left for left, right in zip(values, values[1:], strict=False)]

