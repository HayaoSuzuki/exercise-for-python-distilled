"""0153: テキストのエントロピーのリファレンス実装。"""

from collections import Counter
from math import log2


def entropy(text: str) -> float:
    """text の文字単位のシャノンエントロピー（ビット）を返す。"""
    if not text:
        return 0.0
    n = len(text)
    h = 0.0
    for count in Counter(text).values():
        p = count / n
        h -= p * log2(p)
    return h
