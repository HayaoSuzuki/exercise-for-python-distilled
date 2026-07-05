from itertools import islice

import pytest

from references.ch06 import p0650_prime_stream as primes_mod
from tests._helpers import simple_is_prime


def test_prime_stream_starts_with_first_ten_primes() -> None:
    # Arrange

    # Act
    actual = list(islice(primes_mod.primes(), 10))

    # Assert
    assert actual == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


@pytest.mark.parametrize("index", [0, 9, 99])
def test_prime_stream_generated_values_are_prime(index: int) -> None:
    # Arrange

    # Act
    actual = next(islice(primes_mod.primes(), index, None))

    # Assert
    assert simple_is_prime(actual) is True

