import pytest

from references.ch05 import p0550_function_composition as compose_mod


def test_compose_applies_functions_from_right_to_left() -> None:
    # Arrange
    def increment(x: int) -> int:
        return x + 1

    def double(x: int) -> int:
        return x * 2

    # Act
    actual = compose_mod.compose(double, increment)(5)

    # Assert
    assert actual == 12


def test_compose_without_functions_returns_identity() -> None:
    # Arrange

    # Act
    actual = compose_mod.compose()(42)

    # Assert
    assert actual == 42


@pytest.mark.parametrize(("n", "expected"), [(0, 1), (1, 2), (10, 1024)])
def test_iterate_applies_function_n_times(n: int, expected: int) -> None:
    # Arrange
    def double(x: int) -> int:
        return x * 2

    # Act
    actual = compose_mod.iterate(double, n)(1)

    # Assert
    assert actual == expected


def test_iterate_rejects_negative_count() -> None:
    # Arrange
    count = -1

    # Act
    with pytest.raises(ValueError) as exc_info:
        compose_mod.iterate(lambda x: x, count)

    # Assert
    assert "non-negative" in str(exc_info.value)
