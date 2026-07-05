"""0400: 座標を表す小さなプロトコルのリファレンス実装。"""

from __future__ import annotations

from collections.abc import Iterator


class Point2D:
    """2次元の点。"""

    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point2D({self.x!r}, {self.y!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return 2

    def __iter__(self) -> Iterator[float]:
        yield self.x
        yield self.y
