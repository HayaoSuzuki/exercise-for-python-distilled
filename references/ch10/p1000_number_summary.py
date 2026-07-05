"""1000: 数値列の要約のリファレンス実装。"""

from collections.abc import Iterable


def summarize_numbers(values: Iterable[int]) -> dict[str, int | None]:
    """整数列の個数、合計、最小値、最大値を返す。"""
    numbers = list(values)
    if not numbers:
        return {"count": 0, "total": 0, "min": None, "max": None}
    return {
        "count": len(numbers),
        "total": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
    }
