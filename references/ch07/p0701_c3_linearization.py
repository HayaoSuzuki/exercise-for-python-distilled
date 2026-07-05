"""0701: C3線型化の実装（リファレンス実装）。"""

from __future__ import annotations


def _merge(name: str, sequences: list[list[str]]) -> list[str]:
    """C3 のマージ規則で列を統合する。統合できなければ TypeError を送出する。"""
    result: list[str] = []
    seqs = [seq for seq in ([*s] for s in sequences) if seq]
    while seqs:
        for candidate in (seq[0] for seq in seqs):
            if all(candidate not in seq[1:] for seq in seqs):
                break
        else:
            raise TypeError(
                f"Cannot create a consistent method resolution order (MRO) for {name}"
            )
        result.append(candidate)
        seqs = [seq for seq in ([c for c in seq if c != candidate] for seq in seqs) if seq]
    return result


def linearize(name: str, graph: dict[str, list[str]]) -> list[str]:
    """継承グラフ graph におけるクラス name の C3 線型化（MRO）を返す。"""
    memo: dict[str, list[str]] = {}
    visiting: set[str] = set()

    def visit(cls: str) -> list[str]:
        if cls in memo:
            return [*memo[cls]]
        if cls in visiting:
            raise TypeError(
                f"Cannot create a consistent method resolution order (MRO) for {cls}"
            )
        visiting.add(cls)
        try:
            bases = graph[cls]
            if not bases:
                result = [cls]
            else:
                tails = [visit(base) for base in bases]
                result = [cls, *_merge(cls, [*tails, [*bases]])]
        finally:
            visiting.remove(cls)
        memo[cls] = result
        return [*result]

    return visit(name)
