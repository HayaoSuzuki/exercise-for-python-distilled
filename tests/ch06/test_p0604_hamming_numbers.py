from itertools import islice

from references.ch06 import p0604_hamming_numbers as hamming_mod


def test_hamming_starts_with_first_fifteen_values() -> None:
    # Arrange

    # Act
    actual = list(islice(hamming_mod.hamming(), 15))

    # Assert
    assert actual == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]


def test_hamming_values_are_unique_and_sorted() -> None:
    # Arrange

    # Act
    actual = list(islice(hamming_mod.hamming(), 50))

    # Assert
    assert actual == sorted(set(actual))

