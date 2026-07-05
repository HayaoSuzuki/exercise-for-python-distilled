import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch01 import p0101_repeating_decimal as dec
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("p", "q", "expected"),
    [
        (1, 7, "142857"),
        (1, 6, "6"),
        (22, 7, "142857"),
        (1, 12, "3"),
    ],
)
def test_repetend_returns_repeating_part(p: int, q: int, expected: str) -> None:
    # Arrange

    # Act
    actual = dec.repetend(p, q)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(("p", "q"), [(3, 8), (1, 2), (0, 7)])
def test_repetend_returns_empty_string_for_terminating_decimal(p: int, q: int) -> None:
    # Arrange

    # Act
    actual = dec.repetend(p, q)

    # Assert
    assert actual == ""


@FAST
@given(st.integers(min_value=0, max_value=10_000), st.integers(min_value=1, max_value=500))
def test_repetend_matches_remainder_cycle(p: int, q: int) -> None:
    # Arrange
    seen: dict[int, int] = {}
    digits: list[str] = []
    remainder = p % q
    while remainder and remainder not in seen:
        seen[remainder] = len(digits)
        remainder *= 10
        digits.append(str(remainder // q))
        remainder %= q
    expected = "" if remainder == 0 else "".join(digits[seen[remainder] :])

    # Act
    actual = dec.repetend(p, q)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(("p", "q"), [(-1, 7), (1, 0)])
def test_repetend_rejects_invalid_fraction(p: int, q: int) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        dec.repetend(p, q)

    # Assert
    assert "p must be >= 0 and q must be >= 1" in str(exc_info.value)
