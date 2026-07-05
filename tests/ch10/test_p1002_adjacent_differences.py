import pytest

from references.ch10 import p1002_adjacent_differences as diff_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([10, 13, 9, 9], [3, -4, 0]),
        ([5], []),
        ([], []),
    ],
)
def test_adjacent_differences_returns_neighbor_differences(
    values: list[int], expected: list[int]
) -> None:
    # Arrange

    # Act
    actual = diff_mod.adjacent_differences(values)

    # Assert
    assert actual == expected


def test_adjacent_differences_accepts_tuples() -> None:
    # Arrange
    values = (1, 4, 10)

    # Act
    actual = diff_mod.adjacent_differences(values)

    # Assert
    assert actual == [3, 6]


def test_adjacent_differences_does_not_modify_input_list() -> None:
    # Arrange
    values = [1, 4, 10]

    # Act
    diff_mod.adjacent_differences(values)

    # Assert
    assert values == [1, 4, 10]
