"""0101: 行ごとの点数集計のリファレンス実装。"""


def total_scores(text: str) -> dict[str, int]:
    """空白区切りの行を読み取り、名前ごとの点数を合計する。"""
    totals: dict[str, int] = {}
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != 2:
            raise ValueError(f"line must contain a name and a score（行 {line_number}）")
        name, score_text = parts
        try:
            score = int(score_text)
        except ValueError as exc:
            raise ValueError(f"score must be an integer（行 {line_number}）") from exc
        totals[name] = totals.get(name, 0) + score
    return totals
