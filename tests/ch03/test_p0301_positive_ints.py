import pytest

from references.ch03 import p0301_positive_ints as ints_mod


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["10", "-2", "x", "3"], [10, 3]),
        ([" 7 ", "0", "+5"], [7, 5]),
    ],
)
def test_positive_ints_keeps_positive_integer_strings(
    items: list[str], expected: list[int]
) -> None:
    # Arrange

    # Act
    actual = ints_mod.positive_ints(items)

    # Assert
    assert actual == expected


def test_positive_ints_returns_empty_list_for_empty_input() -> None:
    # Arrange
    items: list[str] = []

    # Act
    actual = ints_mod.positive_ints(items)

    # Assert
    assert actual == []


def test_positive_ints_accepts_iterators() -> None:
    # Arrange
    items = (s for s in ["1", "bad", "2"])

    # Act
    actual = ints_mod.positive_ints(items)

    # Assert
    assert actual == [1, 2]


def test_positive_ints_ignores_invalid_values_without_raising() -> None:
    # Arrange
    items = ["bad"]

    # Act
    actual = ints_mod.positive_ints(items)

    # Assert
    assert actual == []
