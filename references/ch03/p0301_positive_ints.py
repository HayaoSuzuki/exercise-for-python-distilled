"""0301: 正の整数だけを取り出すリファレンス実装。"""

from collections.abc import Iterable


def positive_ints(items: Iterable[str]) -> list[int]:
    """正の整数として読める文字列だけを整数にして返す。"""
    result: list[int] = []
    for item in items:
        try:
            value = int(item)
        except ValueError:
            continue
        if value > 0:
            result.append(value)
    return result
