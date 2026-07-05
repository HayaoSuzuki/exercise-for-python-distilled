import pytest

from references.ch01 import p0101_total_scores as scores_mod


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Ada 10\nGrace 7\nAda 3\n", {"Ada": 13, "Grace": 7}),
        ("Alan -2\nAlan 5\n", {"Alan": 3}),
    ],
)
def test_total_scores_sums_scores_by_name(text: str, expected: dict[str, int]) -> None:
    # Arrange

    # Act
    actual = scores_mod.total_scores(text)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("text", ["", "\n  \n"])
def test_total_scores_returns_empty_dict_for_blank_text(text: str) -> None:
    # Arrange

    # Act
    actual = scores_mod.total_scores(text)

    # Assert
    assert actual == {}


def test_total_scores_rejects_malformed_line() -> None:
    # Arrange
    text = "Ada"

    # Act
    with pytest.raises(ValueError) as exc_info:
        scores_mod.total_scores(text)

    # Assert
    assert str(exc_info.value) == "line must contain a name and a score（行 1）"


def test_total_scores_rejects_non_integer_score() -> None:
    # Arrange
    text = "Ada x"

    # Act
    with pytest.raises(ValueError) as exc_info:
        scores_mod.total_scores(text)

    # Assert
    assert str(exc_info.value) == "score must be an integer（行 1）"
