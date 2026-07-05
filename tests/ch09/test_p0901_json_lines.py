import json

import pytest

from references.ch09 import p0901_json_lines as json_lines_mod


def test_load_json_lines_returns_python_values() -> None:
    # Arrange
    text = '{"name": "Ada"}\n[1, 2]\ntrue\n'

    # Act
    actual = json_lines_mod.load_json_lines(text)

    # Assert
    assert actual == [{"name": "Ada"}, [1, 2], True]


@pytest.mark.parametrize("text", ["", "  \n"])
def test_load_json_lines_returns_empty_list_for_blank_text(text: str) -> None:
    # Arrange

    # Act
    actual = json_lines_mod.load_json_lines(text)

    # Assert
    assert actual == []


def test_load_json_lines_ignores_blank_lines() -> None:
    # Arrange
    text = "\n  1\n\n  2\n"

    # Act
    actual = json_lines_mod.load_json_lines(text)

    # Assert
    assert actual == [1, 2]


def test_load_json_lines_raises_json_decode_error_for_invalid_line() -> None:
    # Arrange
    text = "{bad}"

    # Act
    with pytest.raises(json.JSONDecodeError) as exc_info:
        json_lines_mod.load_json_lines(text)

    # Assert
    assert exc_info.value.pos == 1
