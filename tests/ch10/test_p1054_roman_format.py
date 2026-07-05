from typing import Any, cast

import pytest

from references.ch10 import p1054_roman_format as roman_mod


@pytest.mark.parametrize(
    ("value", "spec", "expected"),
    [
        (2026, "r", "MMXXVI"),
        (1994, "r", "MCMXCIV"),
        (42, "d", "42"),
        (9, "", "IX"),
    ],
)
def test_roman_format_returns_expected_text(value: int, spec: str, expected: str) -> None:
    # Arrange
    roman = roman_mod.Roman(value)

    # Act
    actual = format(roman, spec)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("value", [0, 4000])
def test_roman_rejects_values_outside_supported_range(value: int) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        roman_mod.Roman(value)

    # Assert
    assert "range 1 to 3999" in str(exc_info.value)


def test_roman_rejects_non_integer_value() -> None:
    # Arrange
    value = cast("Any", 1.5)

    # Act
    with pytest.raises(TypeError) as exc_info:
        roman_mod.Roman(value)

    # Assert
    assert "value must be an int" in str(exc_info.value)


def test_roman_rejects_unknown_format_code() -> None:
    # Arrange
    roman = roman_mod.Roman(10)

    # Act
    with pytest.raises(ValueError) as exc_info:
        format(roman, "x")

    # Assert
    assert "unknown format code" in str(exc_info.value)
