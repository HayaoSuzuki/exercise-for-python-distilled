"""0705: 代数構造の抽象基底クラス（リファレンス実装）。"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Monoid[T](ABC):
    """モノイド（M, op, e）の抽象基底クラス。"""

    @abstractmethod
    def op(self, a: T, b: T) -> T:
        """結合的な二項演算を適用する。"""

    @abstractmethod
    def identity(self) -> T:
        """単位元を返す。"""

    def power(self, x: T, n: int) -> T:
        """x の n 乗を、op の呼び出し O(log n) 回で計算する。"""
        if n < 0:
            raise ValueError("n must be non-negative")
        result = self.identity()
        base = x
        while n:
            if n & 1:
                result = self.op(result, base)
            n >>= 1
            if n:
                base = self.op(base, base)
        return result
