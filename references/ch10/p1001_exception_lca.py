"""1001: 例外階層の最近共通祖先のリファレンス実装。"""

from __future__ import annotations

from typing import cast


def common_handler(*exc_types: type[BaseException]) -> type[BaseException]:
    """すべての例外クラスを捕捉できる最も特殊な例外クラスを返す。"""
    if not exc_types:
        raise TypeError("at least one exception class is required")
    for exc in exc_types:
        if not (isinstance(exc, type) and issubclass(exc, BaseException)):
            raise TypeError(f"{exc!r} is not an exception class")
    for candidate in exc_types[0].__mro__:
        if all(issubclass(exc, candidate) for exc in exc_types):
            return cast("type[BaseException]", candidate)
    raise AssertionError("unreachable: BaseException is always a common ancestor")
