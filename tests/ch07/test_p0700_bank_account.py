import pytest

from references.ch07 import p0700_bank_account as account_mod


def test_bank_account_exposes_owner_and_balance() -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    actual = (account.owner, account.balance)

    # Assert
    assert actual == ("Ada", 100)


def test_bank_account_deposit_returns_new_balance() -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    actual = account.deposit(40)

    # Assert
    assert actual == 140


def test_bank_account_withdraw_returns_new_balance() -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    actual = account.withdraw(15)

    # Assert
    assert actual == 85


def test_bank_account_from_text_builds_account() -> None:
    # Arrange
    text = "Grace:200"

    # Act
    account = account_mod.BankAccount.from_text(text)

    # Assert
    assert (account.owner, account.balance) == ("Grace", 200)


def test_bank_account_rejects_negative_initial_balance() -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        account_mod.BankAccount("Ada", -1)

    # Assert
    assert str(exc_info.value) == "balance must be non-negative"


@pytest.mark.parametrize("amount", [0, -1])
def test_bank_account_deposit_rejects_non_positive_amount(amount: int) -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    with pytest.raises(ValueError) as exc_info:
        account.deposit(amount)

    # Assert
    assert str(exc_info.value) == "amount must be positive"


def test_bank_account_withdraw_rejects_overdraft() -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    with pytest.raises(ValueError) as exc_info:
        account.withdraw(101)

    # Assert
    assert str(exc_info.value) == "insufficient funds"


def test_bank_account_balance_is_read_only() -> None:
    # Arrange
    account = account_mod.BankAccount("Ada", 100)

    # Act
    with pytest.raises(AttributeError):
        object.__setattr__(account, "balance", 0)

    # Assert
    assert account.balance == 100
