"""0550: 関数合成のモノイド（リファレンス実装）"""

from collections.abc import Callable
from typing import Any


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """funcs を右端から順に適用する合成関数を返す。compose() は恒等写像を返す。"""

    def composed(x: Any) -> Any:
        for f in reversed(funcs):
            x = f(x)
        return x

    return composed


def iterate(f: Callable[[Any], Any], n: int) -> Callable[[Any], Any]:
    """f を n 回合成した関数を返す。n=0 は恒等写像を返す。"""
    if n < 0:
        raise ValueError("n must be non-negative")

    def iterated(x: Any) -> Any:
        for _ in range(n):
            x = f(x)
        return x

    return iterated
