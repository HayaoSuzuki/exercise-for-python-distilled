import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch01 import p0105_integer_sqrt as isqrt_mod
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 0), (1, 1), (15, 3), (16, 4), (10**40, 100000000000000000000)],
)
def test_isqrt_returns_integer_square_root(n: int, expected: int) -> None:
    # Arrange

    # Act
    actual = isqrt_mod.isqrt(n)

    # Assert
    assert actual == expected


@FAST
@given(st.integers(min_value=0, max_value=10**50))
def test_isqrt_matches_math_isqrt(n: int) -> None:
    # Arrange
    expected = math.isqrt(n)

    # Act
    actual = isqrt_mod.isqrt(n)

    # Assert
    assert actual == expected


def test_isqrt_rejects_negative_input() -> None:
    # Arrange
    n = -1

    # Act
    with pytest.raises(ValueError) as exc_info:
        isqrt_mod.isqrt(n)

    # Assert
    assert "isqrt() argument must be nonnegative" in str(exc_info.value)
