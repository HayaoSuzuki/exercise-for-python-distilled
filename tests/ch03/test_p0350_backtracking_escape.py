import pytest

from references.ch03 import p0350_backtracking_escape as queens
from tests._helpers import assert_valid_queens


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (1, [0]),
        (4, [1, 3, 0, 2]),
        (6, [1, 3, 5, 0, 2, 4]),
    ],
)
def test_first_solution_returns_lexicographically_first_solution(
    n: int, expected: list[int]
) -> None:
    # Arrange

    # Act
    actual = queens.first_solution(n)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("n", [4, 6, 8])
def test_first_solution_returns_valid_n_queens_solution(n: int) -> None:
    # Arrange

    # Act
    actual = queens.first_solution(n)

    # Assert
    assert actual is not None
    assert_valid_queens(actual, n)


@pytest.mark.parametrize("n", [2, 3])
def test_first_solution_returns_none_when_unsatisfiable(n: int) -> None:
    # Arrange

    # Act
    actual = queens.first_solution(n)

    # Assert
    assert actual is None


def test_found_exception_carries_solution_as_args() -> None:
    # Arrange
    solution = [1, 3, 0, 2]

    # Act
    exc = queens.Found(solution)

    # Assert
    assert exc.args == ([1, 3, 0, 2],)
