"""0854: from module import * の意味論のリファレンス実装。"""

from collections.abc import Iterable
from typing import cast


def star_exports(
    namespace: dict[str, object],
    all_names: list[str] | None = None,
) -> set[str]:
    """from module import * が束縛する名前の集合を返す。

    all_names、namespace["__all__"] の順で __all__ を探し、どちらもなければ
    アンダースコアで始まらない名前すべてを返す。__all__ に namespace に存在しない
    名前が含まれていたら AttributeError を送出する。
    """
    if all_names is None:
        declared = namespace.get("__all__")
        if declared is not None:
            all_names = list(cast("Iterable[str]", declared))
    if all_names is None:
        return {name for name in namespace if not name.startswith("_")}
    exports: set[str] = set()
    for name in all_names:
        if name not in namespace:
            raise AttributeError(f"module has no attribute {name!r}")
        exports.add(name)
    return exports
