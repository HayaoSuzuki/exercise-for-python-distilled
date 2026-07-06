import pytest

from references.ch07 import p0754_monoid_abc as monoid_mod


class CountingAdd(monoid_mod.Monoid[int]):
    def __init__(self) -> None:
        self.calls = 0

    def op(self, a: int, b: int) -> int:
        self.calls += 1
        return a + b

    def identity(self) -> int:
        return 0


def test_monoid_power_returns_repeated_operation_result() -> None:
    # Arrange
    add = CountingAdd()

    # Act
    actual = add.power(3, 10)

    # Assert
    assert actual == 30


def test_monoid_power_uses_logarithmic_number_of_ops() -> None:
    # Arrange
    add = CountingAdd()

    # Act
    add.power(1, 10**9)

    # Assert
    assert add.calls <= 60


def test_monoid_power_rejects_negative_exponent() -> None:
    # Arrange
    add = CountingAdd()

    # Act
    with pytest.raises(ValueError) as exc_info:
        add.power(5, -1)

    # Assert
    assert str(exc_info.value) == "n must be non-negative"


def test_monoid_power_with_zero_exponent_returns_identity() -> None:
    # Arrange
    add = CountingAdd()

    # Act
    actual = add.power(5, 0)

    # Assert
    assert actual == 0
