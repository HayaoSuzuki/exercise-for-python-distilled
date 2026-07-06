import pytest

from references.ch09 import p0953_regex_lexer as lexer_mod


def test_tokenize_prefers_longest_operator_tokens() -> None:
    # Arrange
    source = "a<=b == c"

    # Act
    actual = lexer_mod.tokenize(source)

    # Assert
    assert actual == [
        ("NAME", "a"),
        ("OP", "<="),
        ("NAME", "b"),
        ("OP", "=="),
        ("NAME", "c"),
    ]


def test_tokenize_returns_number_tokens() -> None:
    # Arrange
    source = "x = 12.5"

    # Act
    actual = lexer_mod.tokenize(source)

    # Assert
    assert actual == [("NAME", "x"), ("OP", "="), ("NUMBER", "12.5")]


def test_tokenize_skips_whitespace_and_newlines() -> None:
    # Arrange
    source = "x\n  y"

    # Act
    actual = lexer_mod.tokenize(source)

    # Assert
    assert actual == [("NAME", "x"), ("NAME", "y")]


@pytest.mark.parametrize(
    ("source", "expected_message"),
    [
        ("x = 1\ny $ 2", "2行3列: 予期しない文字 '$'"),
        ("a $ 1", "1行3列: 予期しない文字 '$'"),
    ],
)
def test_tokenize_reports_error_line_and_column(source: str, expected_message: str) -> None:
    # Arrange

    # Act
    with pytest.raises(SyntaxError) as exc_info:
        lexer_mod.tokenize(source)

    # Assert
    assert str(exc_info.value) == expected_message
