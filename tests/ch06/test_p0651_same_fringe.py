import pytest

from references.ch06 import p0651_same_fringe as fringe_mod


def test_fringe_yields_leaves_from_left_to_right() -> None:
    # Arrange
    tree = (1, (2, 3), ((4,), 5))

    # Act
    actual = list(fringe_mod.fringe(tree))

    # Assert
    assert actual == [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (((1, 2), 3), (1, (2, 3)), True),
        ((1, (2, 3)), (1, 2), False),
        ((1, 2), (1, 2, None), False),
        ((1, 2), (3, 4), False),
    ],
)
def test_same_fringe_compares_leaf_sequences(left: object, right: object, expected: bool) -> None:
    # Arrange

    # Act
    actual = fringe_mod.same_fringe(left, right)

    # Assert
    assert actual is expected
