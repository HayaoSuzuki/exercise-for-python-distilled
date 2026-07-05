"""0401: 半開区間を表すコンテナのリファレンス実装。"""

from __future__ import annotations

from collections.abc import Iterator


class IntRange:
    """整数の半開区間 [start, stop) を表す。"""

    __slots__ = ("start", "stop")

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __repr__(self) -> str:
        return f"IntRange({self.start!r}, {self.stop!r})"

    def __len__(self) -> int:
        return max(0, self.stop - self.start)

    def __contains__(self, value: object) -> bool:
        return isinstance(value, int) and self.start <= value < self.stop

    def __iter__(self) -> Iterator[int]:
        yield from range(self.start, self.stop)
