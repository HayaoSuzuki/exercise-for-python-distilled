"""0601: 固定長に区切るジェネレータのリファレンス実装。"""

from collections.abc import Iterable, Iterator


def chunked(values: Iterable[int], size: int) -> Iterator[tuple[int, ...]]:
    """values を size 個ごとのタプルに区切って生成する。"""
    if size <= 0:
        raise ValueError("size must be positive")

    chunk: list[int] = []
    for value in values:
        chunk.append(value)
        if len(chunk) == size:
            yield tuple(chunk)
            chunk.clear()
    if chunk:
        yield tuple(chunk)
