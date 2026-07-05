"""0250: 内包表記で作る関係代数（リファレンス実装）。"""

from collections.abc import Callable, Sequence
from typing import Any

Row = dict[str, Any]
Relation = list[Row]


def select(rel: Relation, pred: Callable[[Row], bool]) -> Relation:
    """述語 pred を満たす行だけからなる関係を、元の順序を保って返す。"""
    return [dict(row) for row in rel if pred(row)]


def project(rel: Relation, attrs: Sequence[str]) -> Relation:
    """各行を attrs に制限した関係を返す。重複行は最初の出現だけを残す。"""
    unique = {tuple((a, row[a]) for a in attrs): None for row in rel}
    return [dict(items) for items in unique]


def natural_join(r: Relation, s: Relation) -> Relation:
    """共通属性の値がすべて一致する行の組を合成した関係を返す。"""
    if not r or not s:
        return []
    common = [a for a in r[0] if a in s[0]]
    return [
        row | other
        for row in r
        for other in s
        if all(row[a] == other[a] for a in common)
    ]
