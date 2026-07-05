"""1005: __format__ とローマ数字のリファレンス実装。"""

from __future__ import annotations

_SYMBOLS = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


class Roman:
    """1 以上 3999 以下の整数を包み、ローマ数字の書式ミニ言語を提供する。"""

    def __init__(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("value must be an int")
        if not 1 <= value <= 3999:
            raise ValueError("value must be in the range 1 to 3999")
        self.value = value

    def __repr__(self) -> str:
        return f"Roman({self.value})"

    def __format__(self, spec: str) -> str:
        if spec in ("", "r"):
            remaining = self.value
            parts = []
            for weight, symbol in _SYMBOLS:
                count, remaining = divmod(remaining, weight)
                parts.append(symbol * count)
            return "".join(parts)
        if spec == "d":
            return str(self.value)
        raise ValueError(f"unknown format code {spec!r} for Roman")
