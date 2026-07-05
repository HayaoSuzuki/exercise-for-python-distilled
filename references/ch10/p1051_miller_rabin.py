"""1051: 3引数 pow による Miller–Rabin のリファレンス実装。"""

from __future__ import annotations

from collections.abc import Iterable

# n < 3,317,044,064,679,887,385,961,981 で判定が決定的になる底の集合。
_DEFAULT_BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_probable_prime(n: int, bases: Iterable[int] | None = None) -> bool:
    """Miller–Rabin 法で n が素数と見なせるかを判定する。"""
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 2:
        return False
    if n == 2:
        return True
    _, remainder = divmod(n, 2)
    if remainder == 0:
        return False

    # n - 1 = 2**s * d（d は奇数）に分解する。
    d, s = n - 1, 0
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder:
            break
        d, s = quotient, s + 1

    for a in _DEFAULT_BASES if bases is None else bases:
        _, a = divmod(a, n)
        if a == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
