"""0253: スライスで作る完全シャッフル（リファレンス実装）。"""

from typing import Any


def riffle(deck: list[Any]) -> list[Any]:
    """アウトシャッフルを1回適用した新しいリストを返す。"""
    if len(deck) % 2:
        raise ValueError("deck length must be even")
    half = len(deck) // 2
    shuffled: list[Any] = [None] * len(deck)
    shuffled[::2] = deck[:half]
    shuffled[1::2] = deck[half:]
    return shuffled


def shuffle_order(n: int) -> int:
    """n 枚のデッキが初めて元の並びに戻るまでのアウトシャッフルの回数を返す。"""
    if n < 2 or n % 2:
        raise ValueError("n must be an even integer >= 2")
    deck = list(range(n))
    current = riffle(deck)
    count = 1
    while current != deck:
        current = riffle(current)
        count += 1
    return count
