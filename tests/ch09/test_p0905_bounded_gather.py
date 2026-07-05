import asyncio
from collections.abc import Awaitable
from typing import Any

import pytest

from references.ch09 import p0905_bounded_gather as gather_mod


async def _square_after_yield(x: int) -> int:
    await asyncio.sleep(0)
    return x * x


def test_gather_bounded_preserves_input_order() -> None:
    # Arrange
    coros = [_square_after_yield(3), _square_after_yield(1), _square_after_yield(2)]

    # Act
    actual = asyncio.run(gather_mod.gather_bounded(coros, 2))

    # Assert
    assert actual == [9, 1, 4]


def test_gather_bounded_limits_concurrent_tasks() -> None:
    # Arrange
    async def run() -> int:
        running = 0
        peak = 0

        async def tracked(x: int) -> int:
            nonlocal running, peak
            running += 1
            peak = max(peak, running)
            await asyncio.sleep(0)
            running -= 1
            return x

        await gather_mod.gather_bounded([tracked(i) for i in range(5)], 2)
        return peak

    # Act
    actual = asyncio.run(run())

    # Assert
    assert actual == 2


def test_gather_bounded_rejects_non_positive_limit() -> None:
    # Arrange
    coros: list[Awaitable[Any]] = []

    # Act
    with pytest.raises(ValueError) as exc_info:
        asyncio.run(gather_mod.gather_bounded(coros, 0))

    # Assert
    assert "limit は 1 以上" in str(exc_info.value)
