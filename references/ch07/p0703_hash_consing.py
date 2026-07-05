"""0703: メタクラスによるハッシュコンシング（リファレンス実装）。"""

from __future__ import annotations

from typing import Any


class InternMeta(type):
    """同じ位置引数からは同一のインスタンスを返すメタクラス。"""

    def __init__(cls, name: str, bases: tuple[type, ...], namespace: dict[str, Any]) -> None:
        super().__init__(name, bases, namespace)
        # クラスごとに独立したメモ化の表を持たせる
        cls._intern_table: dict[tuple[Any, ...], Any] = {}

    def __call__(cls, *args: Any) -> Any:
        table = cls._intern_table
        try:
            return table[args]
        except KeyError:
            instance = super().__call__(*args)
            table[args] = instance
            return instance
