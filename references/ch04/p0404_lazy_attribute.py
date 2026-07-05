"""0404: 遅延属性のリファレンス実装。"""

from __future__ import annotations

from collections.abc import Callable


class LazyStats:
    """統計量を初回アクセス時にだけ計算し、インスタンス辞書に埋める。"""

    def __init__(self, data: list[int]) -> None:
        self.data = list(data)
        self.computations = 0

    def __getattr__(self, name: str) -> int:
        thunks: dict[str, Callable[[], int]] = {
            "total": lambda: sum(self.data),
            "minimum": lambda: min(self.data),
            "maximum": lambda: max(self.data),
        }
        if name in thunks:
            self.computations += 1
            value = thunks[name]()
            # インスタンス辞書に埋めるので、次回からは __getattr__ が呼ばれない。
            setattr(self, name, value)
            return value
        raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")
