import pytest

from references.ch07 import p0701_bounded_counter as counter_mod


def test_bounded_counter_exposes_initial_value() -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(5, 2)

    # Act
    actual = counter.value

    # Assert
    assert actual == 2


def test_bounded_counter_increment_returns_new_value() -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(5, 2)

    # Act
    actual = counter.increment(2)

    # Assert
    assert actual == 4


def test_bounded_counter_reset_returns_zero() -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(5, 2)

    # Act
    actual = counter.reset()

    # Assert
    assert actual == 0


def test_bounded_counter_rejects_negative_limit() -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        counter_mod.BoundedCounter(-1)

    # Assert
    assert str(exc_info.value) == "limit must be non-negative"


def test_bounded_counter_rejects_initial_value_outside_range() -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        counter_mod.BoundedCounter(2, 3)

    # Assert
    assert str(exc_info.value) == "value must be between 0 and limit"


@pytest.mark.parametrize("amount", [0, -1])
def test_bounded_counter_rejects_non_positive_increment(amount: int) -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(5, 2)

    # Act
    with pytest.raises(ValueError) as exc_info:
        counter.increment(amount)

    # Assert
    assert str(exc_info.value) == "amount must be positive"


def test_bounded_counter_rejects_increment_past_limit() -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(2)

    # Act
    with pytest.raises(ValueError) as exc_info:
        counter.increment(3)

    # Assert
    assert str(exc_info.value) == "counter limit exceeded"


def test_bounded_counter_value_is_read_only() -> None:
    # Arrange
    counter = counter_mod.BoundedCounter(5, 2)

    # Act
    with pytest.raises(AttributeError):
        object.__setattr__(counter, "value", 0)

    # Assert
    assert counter.value == 2
