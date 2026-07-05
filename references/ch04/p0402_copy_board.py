"""0402: 入れ子リストのコピーのリファレンス実装。"""


def copy_board(board: list[list[str]]) -> list[list[str]]:
    """board と行を共有しないコピーを返す。"""
    return [row.copy() for row in board]
