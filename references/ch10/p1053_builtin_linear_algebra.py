"""1053: zip と map の線形代数のリファレンス実装。"""

from __future__ import annotations

from operator import mul

Matrix = tuple[tuple[int, ...], ...]


def transpose(m: Matrix) -> Matrix:
    """転置行列を返す。"""
    return tuple(zip(*m, strict=True))


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    """行列の積 AB を返す。次元が合わなければ ValueError。"""
    if any(len(row) != len(b) for row in a):
        raise ValueError("dimension mismatch: columns of a must equal rows of b")
    bt = transpose(b)
    return tuple(tuple(sum(map(mul, row, col, strict=True)) for col in bt) for row in a)


def mat_pow(m: Matrix, n: int) -> Matrix:
    """正方行列 m の n 乗を、O(log n) 回の行列乗算で返す。"""
    size = len(m)
    if any(len(row) != size for row in m):
        raise ValueError("m must be a square matrix")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")

    result = tuple(tuple(int(i == j) for j in range(size)) for i in range(size))
    square = m
    while n:
        n, remainder = divmod(n, 2)
        if remainder:
            result = mat_mul(result, square)
        if n:
            square = mat_mul(square, square)
    return result


def fib(n: int) -> int:
    """行列累乗で Fibonacci 数 F_n を返す。"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    return mat_pow(((1, 1), (1, 0)), n)[0][1]
