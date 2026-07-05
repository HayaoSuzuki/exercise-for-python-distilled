"""0200: 在庫差分のリファレンス実装。"""


def inventory_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    """2つの在庫辞書から品目ごとの増減を返す。"""
    deltas: dict[str, int] = {}
    for name in sorted(before.keys() | after.keys()):
        delta = after.get(name, 0) - before.get(name, 0)
        if delta:
            deltas[name] = delta
    return deltas
