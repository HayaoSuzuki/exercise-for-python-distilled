"""0504: トランポリンと継続渡し形式（リファレンス実装）"""

from collections.abc import Callable
from typing import Any


def trampoline(f: Callable[..., Any], *args: Any) -> Any:
    """サンク（引数なしの callable）を返し続ける関数 f をループで駆動する。"""
    result: Any = f(*args)
    while callable(result):
        result = result()
    return result
