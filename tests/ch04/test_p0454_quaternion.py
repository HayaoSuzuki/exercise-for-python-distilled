import math
from fractions import Fraction

import pytest

from references.ch04 import p0454_quaternion as quat_mod


@pytest.mark.parametrize(
    ("args", "invalid_name"),
    [
        (("x", 1, 2, 3), "a"),
        ((1, 2.0, 3, 4), "b"),
    ],
)
def test_quaternion_constructor_rejects_non_int_or_fraction_component(
    args: tuple[object, object, object, object], invalid_name: str
) -> None:
    # Arrange

    # Act
    with pytest.raises(TypeError) as exc_info:
        quat_mod.Quaternion(*args)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]

    # Assert
    assert str(exc_info.value) == f"component {invalid_name} must be int or Fraction"


def test_quaternion_add_combines_each_component() -> None:
    # Arrange
    left = quat_mod.Quaternion(1, 2, 3, 4)
    right = quat_mod.Quaternion(5, 6, 7, 8)

    # Act
    actual = left + right

    # Assert
    assert actual == quat_mod.Quaternion(6, 8, 10, 12)


def test_quaternion_right_scalar_multiplication_returns_scaled_components() -> None:
    # Arrange
    value = quat_mod.Quaternion(1, 2, 3, 4)

    # Act
    actual = value * 2

    # Assert
    assert actual == quat_mod.Quaternion(2, 4, 6, 8)


def test_quaternion_abs_returns_euclidean_norm() -> None:
    # Arrange
    value = quat_mod.Quaternion(3, 4, 5, 6)

    # Act
    actual = abs(value)

    # Assert
    assert math.isclose(actual, math.sqrt(3**2 + 4**2 + 5**2 + 6**2))


def test_quaternion_hash_matches_hash_of_component_tuple() -> None:
    # Arrange
    value = quat_mod.Quaternion(1, 2, 3, 4)

    # Act
    actual = hash(value)

    # Assert
    assert actual == hash((1, 2, 3, 4))


def test_quaternion_conjugate_negates_imaginary_components() -> None:
    # Arrange
    value = quat_mod.Quaternion(1, 2, 3, 4)

    # Act
    actual = value.conjugate()

    # Assert
    assert actual == quat_mod.Quaternion(1, -2, -3, -4)


def test_quaternion_inverse_raises_zero_division_error_for_zero_quaternion() -> None:
    # Arrange
    value = quat_mod.Quaternion(0, 0, 0, 0)

    # Act
    with pytest.raises(ZeroDivisionError) as exc_info:
        value.inverse()

    # Assert
    assert str(exc_info.value) == "zero quaternion has no inverse"


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


@pytest.mark.parametrize(
    "value",
    [
        quat_mod.Quaternion(1, 2, 3, 4),
        quat_mod.Quaternion(3, 5, 7, 11),
    ],
)
def test_quaternion_inverse_multiplies_to_one(value: quat_mod.Quaternion) -> None:
    # Arrange

    # Act
    actual = value * value.inverse()

    # Assert
    assert actual == quat_mod.Quaternion(1, 0, 0, 0)
