"""0402: 半順序としての多重集合包含のリファレンス実装。"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable


class Multiset:
    """多重集合。包含関係による半順序を比較演算子で提供する。"""

    def __init__(self, items: Iterable[Hashable] = ()) -> None:
        self._counts = Counter(items)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Multiset):
            return NotImplemented
        return self._counts == other._counts

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Multiset):
            return NotImplemented
        return all(count <= other._counts[item] for item, count in self._counts.items())

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Multiset):
            return NotImplemented
        return self.__le__(other) and self._counts != other._counts
