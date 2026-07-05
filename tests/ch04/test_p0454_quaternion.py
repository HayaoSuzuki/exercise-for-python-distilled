from fractions import Fraction

import pytest

from references.ch04 import p0454_quaternion as quat_mod


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (
            quat_mod.Quaternion(0, 1, 0, 0),
            quat_mod.Quaternion(0, 0, 1, 0),
            quat_mod.Quaternion(0, 0, 0, 1),
        ),
        (
            quat_mod.Quaternion(0, 0, 1, 0),
            quat_mod.Quaternion(0, 1, 0, 0),
            quat_mod.Quaternion(0, 0, 0, -1),
        ),
    ],
)
def test_quaternion_multiplication_is_order_sensitive(
    left: quat_mod.Quaternion, right: quat_mod.Quaternion, expected: quat_mod.Quaternion
) -> None:
    # Arrange

    # Act
    actual = left * right

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    ("scalar", "expected"),
    [
        (2, quat_mod.Quaternion(2, 4, 6, 8)),
        (Fraction(1, 2), quat_mod.Quaternion(Fraction(1, 2), 1, Fraction(3, 2), 2)),
    ],
)
def test_quaternion_left_scalar_multiplication_returns_scaled_components(
    scalar: int | Fraction, expected: quat_mod.Quaternion
) -> None:
    # Arrange
    value = quat_mod.Quaternion(1, 2, 3, 4)

    # Act
    actual = scalar * value

    # Assert
    assert actual == expected


def test_quaternion_inverse_multiplies_to_one() -> None:
    # Arrange
    value = quat_mod.Quaternion(1, 2, 3, 4)

    # Act
    actual = value * value.inverse()

    # Assert
    assert actual == quat_mod.Quaternion(1, 0, 0, 0)
