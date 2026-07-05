import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch02 import p0205_inclusion_exclusion as coprime_mod
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("n", "primes", "expected"),
    [(30, [2, 3, 5], 8), (100, [2, 3, 5, 7], 22), (10, [], 10), (0, [2], 0)],
)
def test_count_coprimes_returns_literal_examples(
    n: int, primes: list[int], expected: int
) -> None:
    # Arrange

    # Act
    actual = coprime_mod.count_coprimes(n, primes)

    # Assert
    assert actual == expected


@FAST
@given(
    st.integers(min_value=0, max_value=300),
    st.lists(st.sampled_from([2, 3, 5, 7, 11]), unique=True),
)
def test_count_coprimes_matches_brute_force(n: int, primes: list[int]) -> None:
    # Arrange
    expected = sum(1 for k in range(1, n + 1) if all(k % p for p in primes))

    # Act
    actual = coprime_mod.count_coprimes(n, primes)

    # Assert
    assert actual == expected

