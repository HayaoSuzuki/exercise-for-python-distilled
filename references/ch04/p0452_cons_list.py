"""0452: 不変連結リストのリファレンス実装。"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class ConsList:
    """cons セルによるイミュータブルな単方向連結リスト。"""

    __slots__ = ("_head", "_length", "_tail")

    _head: Any
    _tail: ConsList
    _length: int

    def __init__(self) -> None:
        object.__setattr__(self, "_head", None)
        object.__setattr__(self, "_tail", self)
        object.__setattr__(self, "_length", 0)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("ConsList is immutable")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("ConsList is immutable")

    def cons(self, item: Any) -> ConsList:
        """先頭に item を積んだ新しいリストを返す。self は共有され、変更されない。"""
        node = ConsList.__new__(ConsList)
        object.__setattr__(node, "_head", item)
        object.__setattr__(node, "_tail", self)
        object.__setattr__(node, "_length", self._length + 1)
        return node

    @property
    def head(self) -> Any:
        if self._length == 0:
            raise ValueError("empty ConsList has no head")
        return self._head

    @property
    def tail(self) -> ConsList:
        if self._length == 0:
            raise ValueError("empty ConsList has no tail")
        return self._tail

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Iterator[Any]:
        node = self
        while node._length:
            yield node._head
            node = node._tail

    def __contains__(self, item: object) -> bool:
        return any(x == item for x in self)

    def __getitem__(self, index: int) -> Any:
        if not isinstance(index, int):
            raise TypeError("ConsList indices must be integers")
        if not 0 <= index < self._length:
            raise IndexError("ConsList index out of range")
        node = self
        for _ in range(index):
            node = node._tail
        return node._head
