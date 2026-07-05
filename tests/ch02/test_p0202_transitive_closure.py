from hypothesis import given
from hypothesis import strategies as st

from references.ch02 import p0202_transitive_closure as tc
from tests._helpers import FAST


@FAST
@given(st.sets(st.tuples(st.integers(0, 5), st.integers(0, 5)), max_size=12))
def test_transitive_closure_contains_all_input_edges(edges: set[tuple[int, int]]) -> None:
    # Arrange

    # Act
    actual = tc.transitive_closure(edges)

    # Assert
    assert edges <= actual


@FAST
@given(st.sets(st.tuples(st.integers(0, 5), st.integers(0, 5)), max_size=12))
def test_transitive_closure_is_closed_under_path_composition(edges: set[tuple[int, int]]) -> None:
    # Arrange

    # Act
    actual = tc.transitive_closure(edges)

    # Assert
    assert all((a, d) in actual for a, b in actual for c, d in actual if b == c)


def test_transitive_closure_matches_literal_chain_example() -> None:
    # Arrange
    edges = {(1, 2), (2, 3), (3, 4)}

    # Act
    actual = sorted(tc.transitive_closure(edges))

    # Assert
    assert actual == [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

