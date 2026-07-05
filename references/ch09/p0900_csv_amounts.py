"""0900: CSV の金額集計のリファレンス実装。"""

import csv
from io import StringIO

_REQUIRED_COLUMNS = {"name", "amount"}


def sum_csv_amounts(text: str) -> dict[str, int]:
    """CSV 文字列から名前ごとの金額を合計する。"""
    if not text.strip():
        return {}

    reader = csv.DictReader(StringIO(text))
    if reader.fieldnames is None or not set(reader.fieldnames) >= _REQUIRED_COLUMNS:
        raise ValueError("CSV must contain name and amount columns")

    totals: dict[str, int] = {}
    for row in reader:
        name = row.get("name")
        amount_text = row.get("amount")
        if name is None or amount_text is None:
            raise ValueError("CSV must contain name and amount columns")
        totals[name] = totals.get(name, 0) + int(amount_text)
    return totals
