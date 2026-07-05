"""0103: スタック2つで作るキューのリファレンス実装。"""


class Queue[T]:
    """list 2本による FIFO キュー。enqueue/dequeue は償却 O(1)。"""

    def __init__(self) -> None:
        self._incoming: list[T] = []
        self._outgoing: list[T] = []

    def enqueue(self, item: T) -> None:
        """item をキューの末尾に追加する。"""
        self._incoming.append(item)

    def dequeue(self) -> T:
        """キューの先頭の要素を取り除いて返す。空なら IndexError。"""
        if not self._outgoing:
            while self._incoming:
                self._outgoing.append(self._incoming.pop())
        if not self._outgoing:
            raise IndexError("dequeue from empty queue")
        return self._outgoing.pop()

    def __len__(self) -> int:
        return len(self._incoming) + len(self._outgoing)
