import pytest

from references.ch02 import p0200_inventory_delta as delta_mod


@pytest.mark.parametrize(
    ("before", "after", "expected"),
    [
        ({}, {"tea": 4}, {"tea": 4}),
        ({"apple": 3, "book": 1}, {"apple": 5, "pen": 2}, {"apple": 2, "book": -1, "pen": 2}),
    ],
)
def test_inventory_delta_returns_item_changes(
    before: dict[str, int], after: dict[str, int], expected: dict[str, int]
) -> None:
    # Arrange

    # Act
    actual = delta_mod.inventory_delta(before, after)

    # Assert
    assert actual == expected


def test_inventory_delta_omits_unchanged_items() -> None:
    # Arrange
    before = {"tea": 4}
    after = {"tea": 4}

    # Act
    actual = delta_mod.inventory_delta(before, after)

    # Assert
    assert actual == {}


def test_inventory_delta_sorts_result_keys() -> None:
    # Arrange
    before = {"z": 1}
    after = {"a": 1, "z": 2}

    # Act
    actual = list(delta_mod.inventory_delta(before, after))

    # Assert
    assert actual == ["a", "z"]


def test_inventory_delta_does_not_mutate_inputs() -> None:
    # Arrange
    before = {"apple": 3}
    after = {"apple": 5}

    # Act
    delta_mod.inventory_delta(before, after)

    # Assert
    assert before == {"apple": 3}
    assert after == {"apple": 5}
