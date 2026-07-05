"""0501: 引数を束ねるレコード関数のリファレンス実装。"""

_RESERVED_KEYS = {"name", "tags"}


def make_record(
    name: str, /, *tags: str, active: bool = True, **attrs: object
) -> dict[str, object]:
    """位置引数、タグ、状態、任意属性を1つの辞書にまとめる。"""
    for key in attrs:
        if key in _RESERVED_KEYS:
            raise ValueError(f"reserved attribute: {key}")

    record: dict[str, object] = {
        "name": name,
        "tags": tags,
        "active": active,
    }
    record.update(attrs)
    return record
