"""0603: send で更新する平均値のリファレンス実装。"""

from collections.abc import Generator


def running_average() -> Generator[float | None, float | None]:
    count = 0
    total = 0.0
    average: float | None = None
    while True:
        value = yield average
        if value is None:
            continue
        count += 1
        total += value
        average = total / count
