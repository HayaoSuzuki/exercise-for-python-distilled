from references.ch04 import p0401_int_range as range_mod


def test_int_range_repr_uses_bounds() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = repr(interval)

    # Assert
    assert actual == "IntRange(2, 5)"


def test_int_range_len_returns_number_of_values() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = len(interval)

    # Assert
    assert actual == 3


def test_int_range_contains_values_inside_bounds() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = 3 in interval

    # Assert
    assert actual is True


def test_int_range_contains_start_bound() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = 2 in interval

    # Assert
    assert actual is True


def test_int_range_rejects_stop_bound() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = 5 in interval

    # Assert
    assert actual is False


def test_int_range_iterates_values_in_order() -> None:
    # Arrange
    interval = range_mod.IntRange(2, 5)

    # Act
    actual = list(interval)

    # Assert
    assert actual == [2, 3, 4]


def test_int_range_treats_reversed_bounds_as_empty() -> None:
    # Arrange
    interval = range_mod.IntRange(5, 2)

    # Act
    actual = list(interval)

    # Assert
    assert actual == []


def test_int_range_len_treats_reversed_bounds_as_zero() -> None:
    # Arrange
    interval = range_mod.IntRange(5, 2)

    # Act
    actual = len(interval)

    # Assert
    assert actual == 0


def test_int_range_len_treats_empty_bounds_as_zero() -> None:
    # Arrange
    interval = range_mod.IntRange(3, 3)

    # Act
    actual = len(interval)

    # Assert
    assert actual == 0
