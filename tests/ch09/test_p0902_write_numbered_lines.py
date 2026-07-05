from io import StringIO

from references.ch09 import p0902_write_numbered_lines as write_mod


def test_write_numbered_lines_writes_numbered_text() -> None:
    # Arrange
    output = StringIO()

    # Act
    write_mod.write_numbered_lines(["alpha", "beta"], output)

    # Assert
    assert output.getvalue() == "1: alpha\n2: beta\n"


def test_write_numbered_lines_writes_nothing_for_empty_input() -> None:
    # Arrange
    output = StringIO()

    # Act
    write_mod.write_numbered_lines([], output)

    # Assert
    assert output.getvalue() == ""


def test_write_numbered_lines_keeps_line_content_unchanged() -> None:
    # Arrange
    output = StringIO()

    # Act
    write_mod.write_numbered_lines(["  indented  "], output)

    # Assert
    assert output.getvalue() == "1:   indented  \n"
