"""0602: same fringe 問題（yield from による遅延走査の合流）。"""

from __future__ import annotations

from collections.abc import Iterator
from itertools import zip_longest
from typing import Any

_MISSING = object()


def fringe(tree: Any) -> Iterator[Any]:
    """入れ子タプルで表した木の葉を左から右の順に生成する。"""
    if isinstance(tree, tuple):
        for subtree in tree:
            yield from fringe(subtree)
    else:
        yield tree


def same_fringe(t1: Any, t2: Any) -> bool:
    """2つの木のフリンジ（葉の列）が等しいかを遅延走査で判定する。

    両方のフリンジを同時に1葉ずつ進め、最初の不一致で打ち切る。
    葉の枚数が異なる場合は番兵 _MISSING との比較で False になる。
    """
    pairs = zip_longest(fringe(t1), fringe(t2), fillvalue=_MISSING)
    return all(a is not _MISSING and b is not _MISSING and a == b for a, b in pairs)
