"""0254: ジェネレータ式と包除原理（リファレンス実装）。"""

from collections.abc import Sequence


def count_coprimes(n: int, primes: Sequence[int]) -> int:
    """1 以上 n 以下の整数のうち、primes のどの素数でも割り切れないものの個数を返す。"""
    return sum(1 for k in range(1, n + 1) if all(k % p for p in primes))
