"""0753: 弱参照キャッシュ（リファレンス実装）。"""

from __future__ import annotations

import weakref


class Node:
    """名前を持つノード。"""

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Node({self.name!r})"


class NodeCache:
    """強参照を持たないノードのキャッシュ。"""

    def __init__(self) -> None:
        self._cache: weakref.WeakValueDictionary[str, Node] = weakref.WeakValueDictionary()

    def get(self, name: str) -> Node:
        """名前 name のノードを返す。生存していなければ新しく生成して登録する。"""
        try:
            return self._cache[name]
        except KeyError:
            node = Node(name)
            self._cache[name] = node
            return node

    def __contains__(self, name: str) -> bool:
        return name in self._cache

    def __len__(self) -> int:
        return len(self._cache)
