"""0500: 状態を持つ累算関数のリファレンス実装。"""

from collections.abc import Callable


def make_accumulator(initial: int = 0) -> Callable[[int], int]:
    """呼び出しごとに内部の合計を更新する関数を返す。"""
    total = initial

    def add(value: int) -> int:
        nonlocal total
        total += value
        return total

    return add
