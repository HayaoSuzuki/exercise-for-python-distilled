"""0251: 集合演算による推移閉包（リファレンス実装）。"""

from collections.abc import Hashable


def transitive_closure[T: Hashable](edges: set[tuple[T, T]]) -> set[tuple[T, T]]:
    """辺集合 edges の推移閉包を不動点反復で求めて新しい set として返す。"""
    closure = set(edges)
    while True:
        expanded = closure | {
            (a, d) for (a, b) in closure for (c, d) in closure if b == c
        }
        if expanded == closure:
            return closure
        closure = expanded
