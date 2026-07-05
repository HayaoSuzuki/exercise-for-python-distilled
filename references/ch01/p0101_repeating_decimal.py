"""0101: 循環小数の循環節のリファレンス実装。"""


def repetend(p: int, q: int) -> str:
    """分数 p/q の十進小数展開の循環節を返す。有限小数なら空文字列。"""
    if p < 0 or q < 1:
        raise ValueError("p must be >= 0 and q must be >= 1")
    seen: dict[int, int] = {}
    digits: list[str] = []
    r = p % q
    while r != 0 and r not in seen:
        seen[r] = len(digits)
        r *= 10
        digits.append(str(r // q))
        r %= q
    if r == 0:
        return ""
    return "".join(digits[seen[r] :])
