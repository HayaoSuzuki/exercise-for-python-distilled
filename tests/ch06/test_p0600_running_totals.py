import pytest

from references.ch06 import p0600_running_totals as totals_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, -1, 4], [3, 2, 6]),
        ([1, 2, 3], [1, 3, 6]),
    ],
)
def test_running_totals_yields_cumulative_sums(values: list[int], expected: list[int]) -> None:
    # Arrange

    # Act
    actual = list(totals_mod.running_totals(values))

    # Assert
    assert actual == expected


def test_running_totals_yields_nothing_for_empty_input() -> None:
    # Arrange
    values: list[int] = []

    # Act
    actual = list(totals_mod.running_totals(values))

    # Assert
    assert actual == []


def test_running_totals_accepts_iterators() -> None:
    # Arrange
    values = (x for x in [1, 2, 3])

    # Act
    actual = list(totals_mod.running_totals(values))

    # Assert
    assert actual == [1, 3, 6]


def test_running_totals_returns_iterator_consumed_one_value_at_a_time() -> None:
    # Arrange
    iterator = totals_mod.running_totals([1, 2, 3])

    # Act
    actual = next(iterator)

    # Assert
    assert actual == 1
