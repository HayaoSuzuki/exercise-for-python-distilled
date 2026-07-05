from typing import Any, cast

import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch10 import p1051_miller_rabin as mr_mod
from tests._helpers import FAST, simple_is_prime


@pytest.mark.parametrize("n", [2, 3, 5, 37, 7919])
def test_miller_rabin_accepts_known_primes(n: int) -> None:
    # Arrange

    # Act
    actual = mr_mod.is_probable_prime(n)

    # Assert
    assert actual is True


@pytest.mark.parametrize("n", [-1, 0, 1, 4, 9, 221, 341])
def test_miller_rabin_rejects_known_composites(n: int) -> None:
    # Arrange

    # Act
    actual = mr_mod.is_probable_prime(n)

    # Assert
    assert actual is False


def test_miller_rabin_uses_supplied_bases() -> None:
    # Arrange

    # Act
    actual = mr_mod.is_probable_prime(2047, bases=[2])

    # Assert
    assert actual is True


@FAST
@given(st.integers(min_value=-1000, max_value=20_000))
def test_miller_rabin_matches_trial_division_on_small_numbers(n: int) -> None:
    # Arrange

    # Act
    actual = mr_mod.is_probable_prime(n)

    # Assert
    assert actual == simple_is_prime(n)


def test_miller_rabin_rejects_non_integer_input() -> None:
    # Arrange
    n = cast("Any", 3.14)

    # Act
    with pytest.raises(TypeError) as exc_info:
        mr_mod.is_probable_prime(n)

    # Assert
    assert "n must be an int" in str(exc_info.value)
