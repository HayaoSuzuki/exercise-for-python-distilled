"""0154: ニュートン法による整数平方根のリファレンス実装。"""


def isqrt(n: int) -> int:
    """floor(sqrt(n)) を整数演算のみで返す。n が負なら ValueError。"""
    if n < 0:
        raise ValueError("isqrt() argument must be nonnegative")
    if n == 0:
        return 0
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
