import pytest

from references.ch10 import p1000_number_summary as summary_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3, 1, 4], {"count": 3, "total": 8, "min": 1, "max": 4}),
        ([10, -2, 5], {"count": 3, "total": 13, "min": -2, "max": 10}),
    ],
)
def test_summarize_numbers_returns_count_total_min_and_max(
    values: list[int], expected: dict[str, int | None]
) -> None:
    # Arrange

    # Act
    actual = summary_mod.summarize_numbers(values)

    # Assert
    assert actual == expected


def test_summarize_numbers_returns_none_bounds_for_empty_input() -> None:
    # Arrange
    values: list[int] = []

    # Act
    actual = summary_mod.summarize_numbers(values)

    # Assert
    assert actual == {"count": 0, "total": 0, "min": None, "max": None}


def test_summarize_numbers_accepts_iterators() -> None:
    # Arrange
    values = (x for x in [10, -2, 5])

    # Act
    actual = summary_mod.summarize_numbers(values)

    # Assert
    assert actual == {"count": 3, "total": 13, "min": -2, "max": 10}
