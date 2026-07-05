from references.ch05 import p0500_accumulator_closure as accumulator_mod


def test_accumulator_adds_values_to_initial_total() -> None:
    # Arrange
    acc = accumulator_mod.make_accumulator(10)

    # Act
    first = acc(5)
    second = acc(-3)

    # Assert
    assert first == 15
    assert second == 12


def test_accumulator_uses_zero_as_default_initial_total() -> None:
    # Arrange
    acc = accumulator_mod.make_accumulator()

    # Act
    actual = acc(7)

    # Assert
    assert actual == 7


def test_accumulators_keep_independent_state() -> None:
    # Arrange
    left = accumulator_mod.make_accumulator(10)
    right = accumulator_mod.make_accumulator(100)

    # Act
    left_actual = left(1)
    right_actual = right(1)

    # Assert
    assert left_actual == 11
    assert right_actual == 101
