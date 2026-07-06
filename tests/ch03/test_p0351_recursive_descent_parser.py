import pytest

from references.ch03 import p0351_recursive_descent_parser as parser_mod


@pytest.mark.parametrize(
    ("src", "expected"),
    [("1 + 2 * 3", 7), ("(1 + 2) * 3", 9), ("7 / 2", 3.5)],
)
def test_evaluate_returns_value_for_valid_expression(src: str, expected: float) -> None:
    # Arrange

    # Act
    actual = parser_mod.evaluate(src)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    ("source", "expected_message"),
    [
        ("(1 + 2", "expected ')'"),
        ("1 @ 2", "invalid character: '@'"),
        ("", "unexpected end of input"),
        ("+", "unexpected token: '+'"),
        ("1 2", "unexpected token: '2'"),
        ("3 + X", "invalid character: 'X'"),
        ("12X", "invalid character: 'X'"),
    ],
)
def test_evaluate_raises_parse_error_for_syntax_error(
    source: str, expected_message: str
) -> None:
    # Arrange

    # Act
    with pytest.raises(parser_mod.ParseError) as exc_info:
        parser_mod.evaluate(source)

    # Assert
    assert exc_info.type is parser_mod.ParseError
    assert str(exc_info.value) == expected_message


def test_evaluate_chains_zero_division_as_cause() -> None:
    # Arrange
    source = "10 / (3 - 3)"

    # Act
    with pytest.raises(parser_mod.ParseError) as exc_info:
        parser_mod.evaluate(source)

    # Assert
    assert isinstance(exc_info.value.__cause__, ZeroDivisionError)
    assert str(exc_info.value) == "division by zero"
