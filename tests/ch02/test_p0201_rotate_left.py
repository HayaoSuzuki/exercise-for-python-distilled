import pytest

from references.ch02 import p0201_rotate_left as rotate_mod


@pytest.mark.parametrize(
    ("values", "k", "expected"),
    [
        ((1, 2, 3, 4), 1, (2, 3, 4, 1)),
        ((1, 2, 3, 4), 6, (3, 4, 1, 2)),
        ((1, 2, 3, 4), 0, (1, 2, 3, 4)),
    ],
)
def test_rotate_left_returns_rotated_tuple(
    values: tuple[int, ...], k: int, expected: tuple[int, ...]
) -> None:
    # Arrange

    # Act
    actual = rotate_mod.rotate_left(values, k)

    # Assert
    assert actual == expected


def test_rotate_left_returns_empty_tuple_for_empty_input() -> None:
    # Arrange
    values: tuple[int, ...] = ()

    # Act
    actual = rotate_mod.rotate_left(values, 3)

    # Assert
    assert actual == ()


def test_rotate_left_does_not_mutate_input_tuple() -> None:
    # Arrange
    values = (1, 2, 3)

    # Act
    rotate_mod.rotate_left(values, 1)

    # Assert
    assert values == (1, 2, 3)
