import pytest

from references.ch03 import p0302_sum_until_stop as sum_mod


@pytest.mark.parametrize(
    ("lines", "expected"),
    [
        (["10", " 5 ", "", "STOP", "100"], 15),
        (["-2", "3"], 1),
    ],
)
def test_sum_until_stop_adds_integer_lines(lines: list[str], expected: int) -> None:
    # Arrange

    # Act
    actual = sum_mod.sum_until_stop(lines)

    # Assert
    assert actual == expected


def test_sum_until_stop_ignores_blank_lines() -> None:
    # Arrange
    lines = ["", "  ", "4"]

    # Act
    actual = sum_mod.sum_until_stop(lines)

    # Assert
    assert actual == 4


def test_sum_until_stop_does_not_read_after_stop() -> None:
    # Arrange
    lines = ["1", "STOP", "not-an-integer"]

    # Act
    actual = sum_mod.sum_until_stop(lines)

    # Assert
    assert actual == 1


def test_sum_until_stop_rejects_invalid_integer() -> None:
    # Arrange
    lines = ["1", "x"]

    # Act
    with pytest.raises(ValueError) as exc_info:
        sum_mod.sum_until_stop(lines)

    # Assert
    assert str(exc_info.value) == "invalid integer: x"
