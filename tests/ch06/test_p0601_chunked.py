import pytest

from references.ch06 import p0601_chunked as chunked_mod


@pytest.mark.parametrize(
    ("values", "size", "expected"),
    [
        ([1, 2, 3, 4, 5], 2, [(1, 2), (3, 4), (5,)]),
        ([1, 2, 3], 3, [(1, 2, 3)]),
    ],
)
def test_chunked_yields_tuples_of_requested_size(
    values: list[int], size: int, expected: list[tuple[int, ...]]
) -> None:
    # Arrange

    # Act
    actual = list(chunked_mod.chunked(values, size))

    # Assert
    assert actual == expected


def test_chunked_yields_nothing_for_empty_input() -> None:
    # Arrange
    values: list[int] = []

    # Act
    actual = list(chunked_mod.chunked(values, 3))

    # Assert
    assert actual == []


def test_chunked_accepts_iterators() -> None:
    # Arrange
    values = (x for x in [1, 2, 3])

    # Act
    actual = list(chunked_mod.chunked(values, 2))

    # Assert
    assert actual == [(1, 2), (3,)]


def test_chunked_rejects_non_positive_size() -> None:
    # Arrange
    values = [1]

    # Act
    with pytest.raises(ValueError) as exc_info:
        list(chunked_mod.chunked(values, 0))

    # Assert
    assert str(exc_info.value) == "size must be positive"
