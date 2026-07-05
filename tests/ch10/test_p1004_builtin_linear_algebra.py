import pytest

from references.ch10 import p1004_builtin_linear_algebra as matrix_mod


def test_transpose_swaps_rows_and_columns() -> None:
    # Arrange
    matrix = ((1, 2, 3), (4, 5, 6))

    # Act
    actual = matrix_mod.transpose(matrix)

    # Assert
    assert actual == ((1, 4), (2, 5), (3, 6))


def test_mat_mul_returns_matrix_product() -> None:
    # Arrange
    left = ((1, 2), (3, 4))
    right = ((5, 6), (7, 8))

    # Act
    actual = matrix_mod.mat_mul(left, right)

    # Assert
    assert actual == ((19, 22), (43, 50))


def test_mat_pow_returns_power_by_repeated_squaring() -> None:
    # Arrange
    matrix = ((1, 1), (1, 0))

    # Act
    actual = matrix_mod.mat_pow(matrix, 10)

    # Assert
    assert actual == ((89, 55), (55, 34))


def test_fib_returns_literal_fibonacci_number() -> None:
    # Arrange

    # Act
    actual = matrix_mod.fib(100)

    # Assert
    assert actual == 354224848179261915075


def test_mat_mul_rejects_dimension_mismatch() -> None:
    # Arrange
    left = ((1, 2, 3),)
    right = ((1, 2), (3, 4))

    # Act
    with pytest.raises(ValueError) as exc_info:
        matrix_mod.mat_mul(left, right)

    # Assert
    assert "dimension mismatch" in str(exc_info.value)


def test_mat_pow_rejects_non_square_matrix() -> None:
    # Arrange
    matrix = ((1, 2, 3), (4, 5, 6))

    # Act
    with pytest.raises(ValueError) as exc_info:
        matrix_mod.mat_pow(matrix, 2)

    # Assert
    assert "square" in str(exc_info.value)


def test_fib_rejects_negative_index() -> None:
    # Arrange
    n = -1

    # Act
    with pytest.raises(ValueError) as exc_info:
        matrix_mod.fib(n)

    # Assert
    assert "non-negative integer" in str(exc_info.value)

