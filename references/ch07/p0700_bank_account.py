"""0700: 残高を管理するクラスのリファレンス実装。"""

from __future__ import annotations


class BankAccount:
    """所有者名と残高を持つ口座。"""

    def __init__(self, owner: str, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError("balance must be non-negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self) -> int:
        """現在の残高を返す。"""
        return self._balance

    @classmethod
    def from_text(cls, text: str) -> BankAccount:
        """owner:balance 形式の文字列から口座を作る。"""
        owner, balance_text = text.split(":", 1)
        return cls(owner, int(balance_text))

    def deposit(self, amount: int) -> int:
        """正の金額を入金し、新しい残高を返す。"""
        self._check_positive_amount(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount: int) -> int:
        """正の金額を出金し、新しい残高を返す。"""
        self._check_positive_amount(amount)
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        return self._balance

    @staticmethod
    def _check_positive_amount(amount: int) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
