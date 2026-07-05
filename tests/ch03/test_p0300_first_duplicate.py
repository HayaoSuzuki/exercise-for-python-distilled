import pytest

from references.ch03 import p0300_first_duplicate as duplicate_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 1, 3, 1], 3),
        ([2, 1, 1, 2], 1),
        ([-1, 0, -1], -1),
    ],
)
def test_first_duplicate_returns_value_whose_second_appearance_is_leftmost(
    values: list[int], expected: int
) -> None:
    # Arrange

    # Act
    actual = duplicate_mod.first_duplicate(values)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("values", [[], [1, 2, 3]])
def test_first_duplicate_returns_none_when_values_are_unique(values: list[int]) -> None:
    # Arrange

    # Act
    actual = duplicate_mod.first_duplicate(values)

    # Assert
    assert actual is None


def test_first_duplicate_accepts_iterators() -> None:
    # Arrange
    values = (x for x in [4, 5, 4])

    # Act
    actual = duplicate_mod.first_duplicate(values)

    # Assert
    assert actual == 4
