import pytest

from references.ch02 import p0202_even_squares as squares_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1, 2, 3, 4, 5], [4, 16]),
        ([-4, -3, 0, 2], [16, 0, 4]),
    ],
)
def test_even_squares_returns_squares_of_even_values(
    values: list[int], expected: list[int]
) -> None:
    # Arrange

    # Act
    actual = squares_mod.even_squares(values)

    # Assert
    assert actual == expected


def test_even_squares_returns_empty_list_when_no_even_values() -> None:
    # Arrange
    values = [1, 3, 5]

    # Act
    actual = squares_mod.even_squares(values)

    # Assert
    assert actual == []


def test_even_squares_accepts_iterators() -> None:
    # Arrange
    values = (x for x in [1, 2, 6])

    # Act
    actual = squares_mod.even_squares(values)

    # Assert
    assert actual == [4, 36]


def test_even_squares_does_not_modify_input_list() -> None:
    # Arrange
    values = [2, 4]

    # Act
    squares_mod.even_squares(values)

    # Assert
    assert values == [2, 4]
