"""0302: STOP までの合計のリファレンス実装。"""

from collections.abc import Iterable


def sum_until_stop(lines: Iterable[str]) -> int:
    """STOP が現れるまで、整数として読める行を合計する。"""
    total = 0
    for line in lines:
        item = line.strip()
        if item == "":
            continue
        if item == "STOP":
            break
        try:
            total += int(item)
        except ValueError as exc:
            raise ValueError(f"invalid integer: {item}") from exc
    return total
