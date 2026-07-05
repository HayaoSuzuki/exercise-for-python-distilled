import pytest

from references.ch01 import p0102_dedupe as dedupe_mod


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        (["red", "blue", "red", "green", "blue"], ["red", "blue", "green"]),
        (["a", "a", "a"], ["a"]),
    ],
)
def test_dedupe_keeps_first_occurrences(values: list[str], expected: list[str]) -> None:
    # Arrange

    # Act
    actual = dedupe_mod.dedupe(values)

    # Assert
    assert actual == expected


def test_dedupe_returns_empty_list_for_empty_input() -> None:
    # Arrange
    values: list[str] = []

    # Act
    actual = dedupe_mod.dedupe(values)

    # Assert
    assert actual == []


def test_dedupe_accepts_iterators() -> None:
    # Arrange
    values = (x for x in ["a", "a", "b"])

    # Act
    actual = dedupe_mod.dedupe(values)

    # Assert
    assert actual == ["a", "b"]


def test_dedupe_does_not_modify_input_list() -> None:
    # Arrange
    values = ["red", "blue", "red"]

    # Act
    dedupe_mod.dedupe(values)

    # Assert
    assert values == ["red", "blue", "red"]
