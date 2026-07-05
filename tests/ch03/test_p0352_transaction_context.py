import pytest

from references.ch03 import p0352_transaction_context as tx_mod


def test_transaction_keeps_changes_when_block_succeeds() -> None:
    # Arrange
    config = {"host": "localhost", "port": 8080}

    # Act
    with tx_mod.transaction(config) as tx:
        tx["port"] = 80

    # Assert
    assert config == {"host": "localhost", "port": 80}


def test_transaction_rolls_back_changes_when_block_raises() -> None:
    # Arrange
    config = {"host": "localhost", "port": 8080}

    def fail_inside_transaction() -> None:
        with tx_mod.transaction(config) as tx:
            tx["debug"] = True
            del tx["host"]
            raise RuntimeError("rollback")

    # Act
    with pytest.raises(RuntimeError):
        fail_inside_transaction()

    # Assert
    assert config == {"host": "localhost", "port": 8080}
