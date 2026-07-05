"""0706: __slots__ で作る Union-Find（リファレンス実装）。"""

from __future__ import annotations


class DisjointSet:
    """経路圧縮とランクによる併合を行う素集合データ構造。"""

    __slots__ = ("_count", "_parent", "_rank")

    def __init__(self, n: int) -> None:
        if n < 0:
            raise ValueError("n must be non-negative")
        self._parent = list(range(n))
        self._rank = [0] * n
        self._count = n

    @property
    def count(self) -> int:
        """現在の集合の個数を返す。"""
        return self._count

    def _check(self, x: int) -> None:
        if not 0 <= x < len(self._parent):
            raise IndexError(f"element {x} is out of range")

    def find(self, x: int) -> int:
        """x の属する集合の代表元を返す（経路圧縮付き）。"""
        self._check(x)
        root = x
        while self._parent[root] != root:
            root = self._parent[root]
        while self._parent[x] != root:
            self._parent[x], x = root, self._parent[x]
        return root

    def union(self, x: int, y: int) -> bool:
        """x の集合と y の集合を併合する。併合したら True を返す。"""
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self._rank[root_x] < self._rank[root_y]:
            root_x, root_y = root_y, root_x
        self._parent[root_y] = root_x
        if self._rank[root_x] == self._rank[root_y]:
            self._rank[root_x] += 1
        self._count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """x と y が同じ集合に属するかを返す。"""
        return self.find(x) == self.find(y)
