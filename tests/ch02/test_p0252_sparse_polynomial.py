import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch02 import p0252_sparse_polynomial as poly
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("p", "q", "expected"),
    [
        ({2: 1, 0: -1}, {2: -1, 1: 3}, {1: 3, 0: -1}),
        ({2: 1, 0: -1}, {2: -1, 0: 1}, {}),
    ],
)
def test_poly_add_returns_sum_without_zero_terms(
    p: dict[int, int], q: dict[int, int], expected: dict[int, int]
) -> None:
    # Arrange

    # Act
    actual = poly.poly_add(p, q)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    ("p", "q", "expected"),
    [
        ({2: 1, 0: -1}, {2: -1, 1: 3}, {4: -1, 3: 3, 2: 1, 1: -3}),
        # (i=1,j=0) と (i=0,j=1) が同じ次数1に集約され、
        # prod.get(i + j, 0) が既存の加算済み値を返す経路を通る。
        ({1: 2, 0: 3}, {1: 5, 0: 1}, {2: 10, 1: 17, 0: 3}),
    ],
)
def test_poly_mul_returns_convolution_product(
    p: dict[int, int], q: dict[int, int], expected: dict[int, int]
) -> None:
    # Arrange

    # Act
    actual = poly.poly_mul(p, q)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(("p", "x", "expected"), [({2: 1, 0: -1}, 3, 8), ({}, 100, 0)])
def test_poly_eval_returns_value_at_x(p: dict[int, int], x: int, expected: int) -> None:
    # Arrange

    # Act
    actual = poly.poly_eval(p, x)

    # Assert
    assert actual == expected


@FAST
@given(
    st.dictionaries(
        st.integers(0, 8), st.integers(-5, 5).filter(lambda value: value != 0), max_size=5
    ),
    st.dictionaries(
        st.integers(0, 8), st.integers(-5, 5).filter(lambda value: value != 0), max_size=5
    ),
    st.integers(-3, 3),
)
def test_poly_add_evaluation_matches_sum(p: dict[int, int], q: dict[int, int], x: int) -> None:
    # Arrange
    expected = poly.poly_eval(p, x) + poly.poly_eval(q, x)

    # Act
    actual = poly.poly_eval(poly.poly_add(p, q), x)

    # Assert
    assert actual == expected

