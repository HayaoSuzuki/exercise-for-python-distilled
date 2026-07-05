import pytest

from references.ch02 import p0253_riffle_shuffle as riffle_mod


@pytest.mark.parametrize(
    ("deck", "expected"),
    [
        ([1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 2, 6, 3, 7, 4, 8]),
        (["A", "B"], ["A", "B"]),
    ],
)
def test_riffle_returns_out_shuffle(deck: list[object], expected: list[object]) -> None:
    # Arrange

    # Act
    actual = riffle_mod.riffle(deck)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(("n", "expected"), [(2, 1), (8, 3), (52, 8)])
def test_shuffle_order_returns_first_return_to_identity(n: int, expected: int) -> None:
    # Arrange

    # Act
    actual = riffle_mod.shuffle_order(n)

    # Assert
    assert actual == expected


def test_riffle_rejects_odd_length_deck() -> None:
    # Arrange
    deck = [1, 2, 3]

    # Act
    with pytest.raises(ValueError) as exc_info:
        riffle_mod.riffle(deck)

    # Assert
    assert "deck length must be even" in str(exc_info.value)
