"""0602: yield from で一段だけ平坦化のリファレンス実装。"""

from collections.abc import Iterable, Iterator


def flatten_once(groups: Iterable[Iterable[int]]) -> Iterator[int]:
    """内側にある整数を順に生成する。"""
    for group in groups:
        yield from group

