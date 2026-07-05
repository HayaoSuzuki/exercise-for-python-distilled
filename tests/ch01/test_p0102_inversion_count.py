from hypothesis import given
from hypothesis import strategies as st

from references.ch01 import p0102_inversion_count as inv
from tests._helpers import FAST, brute_inversions


@FAST
@given(st.lists(st.integers(min_value=-20, max_value=20), max_size=25))
def test_count_inversions_matches_brute_force(seq: list[int]) -> None:
    # Arrange
    expected = brute_inversions(seq)

    # Act
    actual = inv.count_inversions(seq)

    # Assert
    assert actual == expected


def test_count_inversions_does_not_mutate_input() -> None:
    # Arrange
    seq = [3, 1, 4, 1, 5]

    # Act
    inv.count_inversions(seq)

    # Assert
    assert seq == [3, 1, 4, 1, 5]
