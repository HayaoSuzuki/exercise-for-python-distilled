"""1052: 安定ソートで作る基数ソートのリファレンス実装。"""

from __future__ import annotations


def radix_sort(nums: list[int], base: int = 10) -> list[int]:
    """非負整数のリストを LSD 基数ソートで昇順に並べた新しいリストを返す。"""
    if not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer >= 2")
    if any(not isinstance(n, int) or n < 0 for n in nums):
        raise ValueError("all elements must be non-negative integers")

    result = list(nums)
    if not result:
        return result

    largest = max(result)
    power = 1  # base **（処理済みの桁数）
    while power <= largest:
        result = sorted(result, key=lambda n, p=power: (n // p) % base)
        power *= base
    return result
