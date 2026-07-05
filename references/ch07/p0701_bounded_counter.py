"""0701: 上限付きカウンタのリファレンス実装。"""


class BoundedCounter:
    """0 以上 limit 以下の値を持つカウンタ。"""

    def __init__(self, limit: int, value: int = 0) -> None:
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if not 0 <= value <= limit:
            raise ValueError("value must be between 0 and limit")
        self._limit = limit
        self._value = value

    @property
    def value(self) -> int:
        """現在の値を返す。"""
        return self._value

    def increment(self, amount: int = 1) -> int:
        """値を増やし、新しい値を返す。"""
        if amount <= 0:
            raise ValueError("amount must be positive")
        next_value = self._value + amount
        if next_value > self._limit:
            raise ValueError("counter limit exceeded")
        self._value = next_value
        return self._value

    def reset(self) -> int:
        """値を 0 に戻す。"""
        self._value = 0
        return self._value
