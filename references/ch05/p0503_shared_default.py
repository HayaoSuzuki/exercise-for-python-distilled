"""0503: 共有しないデフォルト引数のリファレンス実装。"""

from collections.abc import Sequence


def add_tag(tag: str, tags: Sequence[str] | None = None) -> list[str]:
    if tags is None:
        return [tag]
    return [*tags, tag]
