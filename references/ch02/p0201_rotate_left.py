"""0201: タプルの左回転のリファレンス実装。"""


def rotate_left(values: tuple[int, ...], k: int) -> tuple[int, ...]:
    """タプルを左へ k 個回転する。"""
    if not values:
        return ()
    offset = k % len(values)
    return values[offset:] + values[:offset]
