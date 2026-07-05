"""0353: NFA のシミュレーション のリファレンス実装。"""


def nfa_accepts[S](
    delta: dict[tuple[S, str], set[S]],
    start: S,
    accepting: set[S],
    s: str,
) -> bool:
    """ε遷移なしの NFA が文字列 s を受理するかどうかを判定する。"""
    states: set[S] = {start}
    for char in s:
        states = {nxt for state in states for nxt in delta.get((state, char), set())}
        if not states:
            return False
    return not states.isdisjoint(accepting)
