"""0554: シグネチャによる自動カリー化（リファレンス実装）"""

import functools
import inspect
from collections.abc import Callable
from typing import Any


def curry(func: Callable[..., Any]) -> Callable[..., Any]:
    """位置引数が仮引数の個数に達するまで部分適用を返すカリー化デコレータ。"""
    signature = inspect.signature(func)
    params = list(signature.parameters.values())
    if not params:
        raise TypeError("curry() requires at least one positional parameter")
    if any(
        param.kind
        not in (inspect.Parameter.POSITIONAL_ONLY, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        or param.default is not inspect.Parameter.empty
        for param in params
    ):
        raise TypeError("curry() supports required positional parameters only")
    arity = len(params)

    def partial_from(collected: tuple[Any, ...]) -> Callable[..., Any]:
        @functools.wraps(func)
        def applied(*args: Any) -> Any:
            new_args = collected + args
            if len(new_args) >= arity:
                return func(*new_args)
            return partial_from(new_args)

        return applied

    return partial_from(())
