import pytest

from references.ch04 import p0450_modular_ring as mod_ring


@pytest.mark.parametrize(
    ("left", "op", "right", "expected"),
    [
        (mod_ring.Mod(3, 7), "+", mod_ring.Mod(5, 7), mod_ring.Mod(1, 7)),
        (mod_ring.Mod(3, 7), "-", mod_ring.Mod(5, 7), mod_ring.Mod(5, 7)),
        (mod_ring.Mod(3, 7), "*", mod_ring.Mod(5, 7), mod_ring.Mod(1, 7)),
    ],
)
def test_mod_arithmetic_returns_value_with_same_modulus(
    left: mod_ring.Mod, op: str, right: mod_ring.Mod, expected: mod_ring.Mod
) -> None:
    # Arrange

    # Act
    if op == "+":
        actual = left + right
    elif op == "-":
        actual = left - right
    else:
        actual = left * right

    # Assert
    assert actual == expected


def test_mod_hash_treats_equal_values_as_one_set_element() -> None:
    # Arrange

    # Act
    actual = len({mod_ring.Mod(3, 7), mod_ring.Mod(10, 7)})

    # Assert
    assert actual == 1


def test_mod_arithmetic_rejects_different_moduli() -> None:
    # Arrange
    left = mod_ring.Mod(1, 5)
    right = mod_ring.Mod(1, 7)

    # Act
    with pytest.raises(TypeError) as exc_info:
        left + right

    # Assert
    assert str(exc_info.value) == "cannot operate on Mod objects with different moduli: 5 and 7"


@pytest.mark.parametrize(
    ("value", "modulus"),
    [
        ("x", 7),
        (3, "x"),
        (3.0, 7),
    ],
)
def test_mod_constructor_rejects_non_int_value_or_modulus(value: object, modulus: object) -> None:
    # Arrange

    # Act
    with pytest.raises(TypeError) as exc_info:
        mod_ring.Mod(value, modulus)  # type: ignore[arg-type]  # ty:ignore[invalid-argument-type]

    # Assert
    assert str(exc_info.value) == "value and modulus must be int"


@pytest.mark.parametrize("modulus", [1, 0, -5])
def test_mod_constructor_rejects_modulus_below_two(modulus: int) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        mod_ring.Mod(3, modulus)

    # Assert
    assert str(exc_info.value) == "modulus must be at least 2"


def test_mod_constructor_accepts_boundary_modulus_of_two() -> None:
    # Arrange

    # Act
    actual = mod_ring.Mod(3, 2)

    # Assert
    assert actual == mod_ring.Mod(1, 2)


@pytest.mark.parametrize(
    ("value", "exponent", "expected"),
    [
        (mod_ring.Mod(3, 7), 2, mod_ring.Mod(2, 7)),
        (mod_ring.Mod(3, 7), -1, mod_ring.Mod(5, 7)),
    ],
)
def test_mod_pow_computes_modular_exponentiation(
    value: mod_ring.Mod, exponent: int, expected: mod_ring.Mod
) -> None:
    # Arrange

    # Act
    actual = value**exponent

    # Assert
    assert actual == expected


def test_mod_pow_with_non_int_exponent_raises_type_error() -> None:
    # Arrange
    value = mod_ring.Mod(3, 7)

    # Act
    with pytest.raises(TypeError):
        value**2.5  # type: ignore[operator]

    # Assert
    assert value == mod_ring.Mod(3, 7)


def test_mod_eq_returns_false_when_moduli_differ_even_if_values_match() -> None:
    # Arrange
    left = mod_ring.Mod(3, 7)
    right = mod_ring.Mod(3, 5)

    # Act
    actual = left == right

    # Assert
    assert actual is False


def test_mod_hash_matches_hash_of_value_and_modulus_tuple() -> None:
    # Arrange
    value = mod_ring.Mod(3, 7)

    # Act
    actual = hash(value)

    # Assert
    assert actual == hash((3, 7))
