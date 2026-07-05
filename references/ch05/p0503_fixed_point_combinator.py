"""0503: 不動点コンビネータ（リファレンス実装）"""

from collections.abc import Callable
from typing import Any


def fix(f: Callable[[Callable[..., Any]], Callable[..., Any]]) -> Callable[..., Any]:
    """Z コンビネータによる不動点コンビネータ。fix 自身の名前による再帰参照を使わない。"""
    return (lambda x: f(lambda *args: x(x)(*args)))(
        lambda x: f(lambda *args: x(x)(*args))
    )
