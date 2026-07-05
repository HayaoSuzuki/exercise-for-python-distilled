"""0702: 合成で作る履歴付きスタックのリファレンス実装。"""

from collections.abc import Iterator


class HistoryStack:
    """push と pop の履歴を残す文字列スタック。"""

    def __init__(self) -> None:
        self._items: list[str] = []
        self.history: list[tuple[str, str]] = []

    def push(self, item: str) -> None:
        self._items.append(item)
        self.history.append(("push", item))

    def pop(self) -> str:
        if not self._items:
            raise IndexError("pop from empty stack")
        item = self._items.pop()
        self.history.append(("pop", item))
        return item

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[str]:
        return iter(self._items)
