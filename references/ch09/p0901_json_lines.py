"""0901: JSON Lines を読むリファレンス実装。"""

import json


def load_json_lines(text: str) -> list[object]:
    """1行に1つの JSON 値があるテキストを読み取る。"""
    return [json.loads(line) for line in text.splitlines() if line.strip()]
