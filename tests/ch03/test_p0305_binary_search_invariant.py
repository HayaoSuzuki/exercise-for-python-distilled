import bisect

import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch03 import p0305_binary_search_invariant as bisect_mod
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("items", "x", "expected"),
    [
        ([1, 3, 3, 5], 3, 1),
        ([1, 3, 3, 5], 4, 3),
        ([], 42, 0),
    ],
)
def test_bisect_left_returns_literal_examples(items: list[int], x: int, expected: int) -> None:
    # Arrange

    # Act
    actual = bisect_mod.bisect_left(items, x)

    # Assert
    assert actual == expected


@FAST
@given(st.lists(st.integers(-20, 20), max_size=50).map(sorted), st.integers(-25, 25))
def test_bisect_left_matches_stdlib(a: list[int], x: int) -> None:
    # Arrange
    expected = bisect.bisect_left(a, x)

    # Act
    actual = bisect_mod.bisect_left(a, x)

    # Assert
    assert actual == expected
