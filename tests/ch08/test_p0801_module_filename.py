import pytest

from references.ch08 import p0801_module_filename as filename_mod


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("spam", "spam.py"),
        ("pkg.tools.reader", "pkg/tools/reader.py"),
    ],
)
def test_module_filename_converts_dotted_name_to_path(name: str, expected: str) -> None:
    # Arrange

    # Act
    actual = filename_mod.module_filename(name)

    # Assert
    assert actual == expected


@pytest.mark.parametrize("name", ["pkg..reader", "class", "pkg.1bad", ""])
def test_module_filename_rejects_invalid_module_name(name: str) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        filename_mod.module_filename(name)

    # Assert
    assert str(exc_info.value) == "invalid module name"
