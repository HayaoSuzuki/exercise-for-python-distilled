import pytest

from references.ch06 import p0602_flatten_once as flatten_mod


@pytest.mark.parametrize(
    ("groups", "expected"),
    [
        ([[1, 2], [], [3]], [1, 2, 3]),
        (((1, 2), (3,)), [1, 2, 3]),
    ],
)
def test_flatten_once_yields_inner_values(groups, expected: list[int]) -> None:
    # Arrange

    # Act
    actual = list(flatten_mod.flatten_once(groups))

    # Assert
    assert actual == expected


def test_flatten_once_accepts_generator_groups() -> None:
    # Arrange
    groups = (range(n) for n in [0, 2, 3])

    # Act
    actual = list(flatten_mod.flatten_once(groups))

    # Assert
    assert actual == [0, 1, 0, 1, 2]


def test_flatten_once_returns_empty_iterator_for_empty_outer_input() -> None:
    # Arrange
    groups: list[list[int]] = []

    # Act
    actual = list(flatten_mod.flatten_once(groups))

    # Assert
    assert actual == []
