"""0502: 呼び出し回数を数えるデコレータのリファレンス実装。"""

from collections.abc import Callable
from functools import update_wrapper


class Counted[**P, R]:
    """呼び出し回数を保持する callable。"""

    __name__: str
    __doc__: str | None
    __module__: str

    def __init__(self, func: Callable[P, R]) -> None:
        self._func = func
        self.calls = 0
        update_wrapper(self, func)

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        self.calls += 1
        return self._func(*args, **kwargs)


def count_calls[**P, R](func: Callable[P, R]) -> Counted[P, R]:
    """func を呼び出し回数付き callable として包む。"""
    return Counted(func)
