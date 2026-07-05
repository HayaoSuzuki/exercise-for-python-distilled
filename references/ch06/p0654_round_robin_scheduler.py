"""0654: ラウンドロビン・スケジューラ（協調的マルチタスク）。"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterator


class Scheduler:
    """ジェネレータを協調的タスクとしてラウンドロビン実行するスケジューラ。"""

    def __init__(self) -> None:
        self._queue: deque[Iterator[object]] = deque()

    def add(self, task: Iterator[object]) -> None:
        """タスク（ジェネレータ）を実行キューの末尾に登録する。"""
        self._queue.append(task)

    def run(self) -> None:
        """キューが空になるまでタスクをラウンドロビンで実行する。

        先頭のタスクを次の yield まで実行し、終了していなければ末尾に戻す。
        StopIteration 以外の例外はそのまま伝播させる。
        """
        while self._queue:
            task = self._queue.popleft()
            try:
                next(task)
            except StopIteration:
                continue
            self._queue.append(task)
