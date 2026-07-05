"""0454: 四元数のリファレンス実装。"""

from __future__ import annotations

import math
from fractions import Fraction

Scalar = int | Fraction


def _normalize(x: Scalar) -> Scalar:
    """整数値の Fraction を int に直し、repr を安定させる。"""
    if isinstance(x, Fraction) and x.denominator == 1:
        return int(x)
    return x


class Quaternion:
    """四元数 a + bi + cj + dk。成分は int または Fraction。"""

    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a: Scalar, b: Scalar, c: Scalar, d: Scalar) -> None:
        for name, x in zip("abcd", (a, b, c, d), strict=True):
            if not isinstance(x, int | Fraction):
                raise TypeError(f"component {name} must be int or Fraction")
        self.a = _normalize(a)
        self.b = _normalize(b)
        self.c = _normalize(c)
        self.d = _normalize(d)

    def __add__(self, other: object) -> Quaternion:
        if not isinstance(other, Quaternion):
            return NotImplemented
        return Quaternion(
            self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d
        )

    def __mul__(self, other: object) -> Quaternion:
        if isinstance(other, int | Fraction):
            return Quaternion(self.a * other, self.b * other, self.c * other, self.d * other)
        if not isinstance(other, Quaternion):
            return NotImplemented
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d
        return Quaternion(
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        )

    def __rmul__(self, other: object) -> Quaternion:
        if not isinstance(other, int | Fraction):
            return NotImplemented
        return Quaternion(other * self.a, other * self.b, other * self.c, other * self.d)

    def __abs__(self) -> float:
        return math.sqrt(self.a**2 + self.b**2 + self.c**2 + self.d**2)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quaternion):
            return NotImplemented
        return (self.a, self.b, self.c, self.d) == (other.a, other.b, other.c, other.d)

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c, self.d))

    def __repr__(self) -> str:
        return f"Quaternion({self.a!r}, {self.b!r}, {self.c!r}, {self.d!r})"

    def conjugate(self) -> Quaternion:
        """共役 a - bi - cj - dk を返す。"""
        return Quaternion(self.a, -self.b, -self.c, -self.d)

    def inverse(self) -> Quaternion:
        """乗法逆元を返す。零四元数なら ZeroDivisionError。"""
        norm_sq = self.a**2 + self.b**2 + self.c**2 + self.d**2
        if norm_sq == 0:
            raise ZeroDivisionError("zero quaternion has no inverse")
        return Quaternion(
            Fraction(self.a) / norm_sq,
            Fraction(-self.b) / norm_sq,
            Fraction(-self.c) / norm_sq,
            Fraction(-self.d) / norm_sq,
        )
