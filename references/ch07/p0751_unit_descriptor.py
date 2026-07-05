"""0751: ディスクリプタで作る単位付き量（リファレンス実装）。"""

from __future__ import annotations


class Quantity:
    """数値と次元（基本単位の指数タプル）を持つ物理量。"""

    def __init__(self, value: float, dim: tuple[int, ...]) -> None:
        self.value = value
        self.dim = dim

    def __repr__(self) -> str:
        return f"Quantity({self.value!r}, {self.dim!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Quantity):
            return NotImplemented
        return self.value == other.value and self.dim == other.dim


class Measured:
    """次元 dim の Quantity だけを受け付けるデータディスクリプタ。"""

    def __init__(self, dim: tuple[int, ...]) -> None:
        self.dim = dim

    def __set_name__(self, cls: type, name: str) -> None:
        self.name = name

    def __get__(self, instance: object, cls: type | None = None) -> Measured | Quantity:
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance: object, value: Quantity) -> None:
        if not isinstance(value, Quantity):
            raise TypeError(f"{self.name} expects a Quantity, got {type(value).__name__}")
        if value.dim != self.dim:
            raise TypeError(f"{self.name} expects dimension {self.dim}, got {value.dim}")
        instance.__dict__[self.name] = value
