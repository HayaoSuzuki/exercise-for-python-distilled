import pytest

from references.ch10 import p1001_top_scores as scores_mod


@pytest.mark.parametrize(
    ("scores", "n", "expected"),
    [
        ({"Ada": 10, "Grace": 12, "Alan": 12}, 2, [("Alan", 12), ("Grace", 12)]),
        ({"Ada": 10, "Grace": 7}, 10, [("Ada", 10), ("Grace", 7)]),
        ({"Ada": 10, "Grace": 12}, 1, [("Grace", 12)]),
    ],
)
def test_top_scores_returns_highest_scores(
    scores: dict[str, int], n: int, expected: list[tuple[str, int]]
) -> None:
    # Arrange

    # Act
    actual = scores_mod.top_scores(scores, n)

    # Assert
    assert actual == expected


def test_top_scores_returns_empty_list_for_empty_input() -> None:
    # Arrange
    scores: dict[str, int] = {}

    # Act
    actual = scores_mod.top_scores(scores, 3)

    # Assert
    assert actual == []


@pytest.mark.parametrize("n", [0, -1])
def test_top_scores_returns_empty_list_for_non_positive_n(n: int) -> None:
    # Arrange
    scores = {"Ada": 10}

    # Act
    actual = scores_mod.top_scores(scores, n)

    # Assert
    assert actual == []


def test_top_scores_does_not_mutate_input_dict() -> None:
    # Arrange
    scores = {"Ada": 10, "Grace": 12}

    # Act
    scores_mod.top_scores(scores, 1)

    # Assert
    assert scores == {"Ada": 10, "Grace": 12}
