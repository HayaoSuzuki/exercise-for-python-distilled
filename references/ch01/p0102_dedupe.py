"""0102: 順序を保つ重複除去のリファレンス実装。"""

from collections.abc import Iterable


def dedupe(values: Iterable[str]) -> list[str]:
    """values から最初に現れた文字列だけを順に残す。"""
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
