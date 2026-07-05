"""0450: 剰余環 Z/nZ のリファレンス実装。"""

from __future__ import annotations


class Mod:
    """法 modulus に関する整数の剰余類。"""

    __slots__ = ("_modulus", "_value")

    def __init__(self, value: int, modulus: int) -> None:
        if not isinstance(value, int) or not isinstance(modulus, int):
            raise TypeError("value and modulus must be int")
        if modulus < 2:
            raise ValueError("modulus must be at least 2")
        self._value = value % modulus
        self._modulus = modulus

    def _check_operand(self, other: object) -> Mod | None:
        """同じ法の Mod なら返す。Mod でなければ None。法が異なれば TypeError。"""
        if not isinstance(other, Mod):
            return None
        if other._modulus != self._modulus:
            raise TypeError(
                "cannot operate on Mod objects with different moduli: "
                f"{self._modulus} and {other._modulus}"
            )
        return other

    def __add__(self, other: object) -> Mod:
        rhs = self._check_operand(other)
        if rhs is None:
            return NotImplemented
        return Mod(self._value + rhs._value, self._modulus)

    def __sub__(self, other: object) -> Mod:
        rhs = self._check_operand(other)
        if rhs is None:
            return NotImplemented
        return Mod(self._value - rhs._value, self._modulus)

    def __mul__(self, other: object) -> Mod:
        rhs = self._check_operand(other)
        if rhs is None:
            return NotImplemented
        return Mod(self._value * rhs._value, self._modulus)

    def __pow__(self, exponent: object) -> Mod:
        if not isinstance(exponent, int):
            return NotImplemented
        # 組み込み pow は負の指数に対して法逆元を計算し、
        # 逆元が存在しなければ ValueError を送出する。
        return Mod(pow(self._value, exponent, self._modulus), self._modulus)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Mod):
            return NotImplemented
        return self._modulus == other._modulus and self._value == other._value

    def __hash__(self) -> int:
        return hash((self._value, self._modulus))

    def __repr__(self) -> str:
        return f"Mod({self._value}, {self._modulus})"
