import pytest

from references.ch08 import p0803_relative_import as relative_mod


@pytest.mark.parametrize(
    ("name", "package", "level", "expected"),
    [
        ("primitive", "graphics.graph2d", 2, "graphics.primitive"),
        ("", "graphics.primitive", 1, "graphics.primitive"),
    ],
)
def test_resolve_name_converts_relative_to_absolute_name(
    name: str, package: str, level: int, expected: str
) -> None:
    # Arrange

    # Act
    actual = relative_mod.resolve_name(name, package, level)

    # Assert
    assert actual == expected


def test_resolve_name_rejects_import_beyond_top_level() -> None:
    # Arrange
    name = "fill"
    package = "graphics"
    level = 2

    # Act
    with pytest.raises(ImportError) as exc_info:
        relative_mod.resolve_name(name, package, level)

    # Assert
    assert "beyond top-level" in str(exc_info.value)
