from typing import Any, cast

import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch10 import p1052_radix_sort as radix_mod
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("nums", "base", "expected"),
    [
        ([], 10, []),
        ([7], 10, [7]),
        ([170, 45, 75, 90, 802, 24, 2, 66], 10, [2, 24, 45, 66, 75, 90, 170, 802]),
        ([15, 3, 8, 0, 3], 2, [0, 3, 3, 8, 15]),
    ],
)
def test_radix_sort_returns_numbers_in_ascending_order(
    nums: list[int], base: int, expected: list[int]
) -> None:
    # Arrange

    # Act
    actual = radix_mod.radix_sort(nums, base)

    # Assert
    assert actual == expected


def test_radix_sort_does_not_mutate_input_list() -> None:
    # Arrange
    nums = [3, 1, 2]

    # Act
    radix_mod.radix_sort(nums)

    # Assert
    assert nums == [3, 1, 2]


@pytest.mark.parametrize("base", [0, 1, 1.5])
def test_radix_sort_rejects_invalid_base(base: object) -> None:
    # Arrange
    nums = [1, 2, 3]

    # Act
    with pytest.raises(ValueError) as exc_info:
        radix_mod.radix_sort(nums, cast("Any", base))

    # Assert
    assert "base must be an integer >= 2" in str(exc_info.value)


@pytest.mark.parametrize("nums", [[-1], [1, 2.5]])
def test_radix_sort_rejects_invalid_elements(nums: list[object]) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        radix_mod.radix_sort(cast("Any", nums))

    # Assert
    assert "all elements must be non-negative integers" in str(exc_info.value)


@FAST
@given(
    st.lists(st.integers(min_value=0, max_value=10_000), max_size=80),
    st.integers(min_value=2, max_value=16),
)
def test_radix_sort_matches_builtin_sorted(nums: list[int], base: int) -> None:
    # Arrange

    # Act
    actual = radix_mod.radix_sort(nums, base)

    # Assert
    assert actual == sorted(nums)
