"""0902: 行番号付き出力のリファレンス実装。"""

from collections.abc import Iterable
from typing import TextIO


def write_numbered_lines(lines: Iterable[str], output: TextIO) -> None:
    """lines に行番号を付けて output へ書き出す。"""
    for number, line in enumerate(lines, 1):
        print(f"{number}: {line}", file=output)
