import pytest

from references.ch04 import p0401_modular_ring as mod_ring


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
    assert "different moduli" in str(exc_info.value)

