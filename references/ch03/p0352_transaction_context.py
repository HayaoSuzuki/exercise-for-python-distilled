"""0352: トランザクションを実現するコンテキストマネージャ のリファレンス実装。"""

from types import TracebackType


class transaction:  # クラス名は問題の仕様に合わせて小文字
    """辞書への変更を、例外発生時にスナップショット時点まで巻き戻すコンテキストマネージャ。"""

    def __init__(self, mapping: dict) -> None:
        self.mapping = mapping
        self.snapshot: dict | None = None

    def __enter__(self) -> dict:
        self.snapshot = dict(self.mapping)
        return self.mapping

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        tb: TracebackType | None,
    ) -> bool:
        if exc_type is not None and self.snapshot is not None:
            self.mapping.clear()
            self.mapping.update(self.snapshot)
        return False
