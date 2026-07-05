"""0905: asyncio による有界並行実行のリファレンス実装。"""

import asyncio
from collections.abc import Awaitable, Iterable
from typing import Any


async def gather_bounded(coros: Iterable[Awaitable[Any]], limit: int) -> list[Any]:
    if limit < 1:
        raise ValueError("limit は 1 以上でなければなりません")
    semaphore = asyncio.Semaphore(limit)

    async def run(coro: Awaitable[Any]) -> Any:
        async with semaphore:
            return await coro

    return await asyncio.gather(*(run(coro) for coro in coros))
