import pytest

from references.ch01 import p0100_word_frequency as frequency_mod


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Spam spam eggs", {"spam": 2, "eggs": 1}),
        ("  one\tone\nTWO  ", {"one": 2, "two": 1}),
    ],
)
def test_word_frequencies_counts_words_case_insensitively(
    text: str, expected: dict[str, int]
) -> None:
    # Arrange

    # Act
    actual = frequency_mod.word_frequencies(text)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("text", ["", "   \n\t  "])
def test_word_frequencies_returns_empty_dict_for_blank_text(text: str) -> None:
    # Arrange

    # Act
    actual = frequency_mod.word_frequencies(text)

    # Assert
    assert actual == {}


def test_word_frequencies_keeps_punctuation_as_part_of_word() -> None:
    # Arrange
    text = "hello, hello"

    # Act
    actual = frequency_mod.word_frequencies(text)

    # Assert
    assert actual == {"hello,": 1, "hello": 1}


def test_word_frequencies_preserves_first_appearance_order() -> None:
    # Arrange
    text = "b a b c"

    # Act
    actual = list(frequency_mod.word_frequencies(text))

    # Assert
    assert actual == ["b", "a", "c"]
