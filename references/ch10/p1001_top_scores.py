"""1001: 上位の点数のリファレンス実装。"""


def top_scores(scores: dict[str, int], n: int) -> list[tuple[str, int]]:
    """点数の高い順に上位 n 件を返す。"""
    if n <= 0:
        return []
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:n]
