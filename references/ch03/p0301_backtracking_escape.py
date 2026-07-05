"""0301: 例外による探索の打ち切り のリファレンス実装。"""


class Found(Exception):
    """解が見つかったことを表す例外。見つかった解を運ぶ。"""

    def __init__(self, solution: list[int]) -> None:
        super().__init__(solution)
        self.solution = solution


def first_solution(n: int) -> list[int] | None:
    """Nクイーン問題の辞書式順序で最初の解を返す。解がなければ None を返す。"""

    def place(row: int, cols: list[int]) -> None:
        if row == n:
            raise Found(cols[:])
        for col in range(n):
            if all(col != c and abs(col - c) != row - r for r, c in enumerate(cols)):
                cols.append(col)
                place(row + 1, cols)
                cols.pop()

    try:
        place(0, [])
    except Found as found:
        return found.solution
    return None
