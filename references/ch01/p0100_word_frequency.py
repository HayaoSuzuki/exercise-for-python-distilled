"""0100: 単語頻度表のリファレンス実装。"""


def word_frequencies(text: str) -> dict[str, int]:
    """空白区切りの単語を小文字化し、出現回数を返す。"""
    counts: dict[str, int] = {}
    for word in text.split():
        key = word.lower()
        counts[key] = counts.get(key, 0) + 1
    return counts
