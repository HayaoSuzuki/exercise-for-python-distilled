"""0502: メモ化デコレータと動的計画法（リファレンス実装）"""

import functools
from collections.abc import Callable
from typing import Any


def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """位置引数をキーとして func の返り値を記録するメモ化デコレータ。"""
    cache: dict[tuple[Any, ...], Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper
