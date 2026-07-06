import pytest

from references.ch08 import p0852_relative_import as relative_mod


@pytest.mark.parametrize(
    ("name", "package", "level", "expected"),
    [
        ("primitive", "graphics.graph2d", 2, "graphics.primitive"),
        ("", "graphics.primitive", 1, "graphics.primitive"),
        ("circle", "graphics.utils.shapes", 2, "graphics.utils.circle"),
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
    assert str(exc_info.value) == "attempted relative import beyond top-level package"


@pytest.mark.parametrize("level", [0, -1])
def test_resolve_name_rejects_level_below_one(level: int) -> None:
    # Arrange
    name = "x"
    package = "pkg"

    # Act
    with pytest.raises(ValueError) as exc_info:
        relative_mod.resolve_name(name, package, level)

    # Assert
    assert str(exc_info.value) == "level must be at least 1"


def test_resolve_name_rejects_empty_package() -> None:
    # Arrange
    name = "x"
    package = ""
    level = 1

    # Act
    with pytest.raises(ImportError) as exc_info:
        relative_mod.resolve_name(name, package, level)

    # Assert
    assert (
        str(exc_info.value)
        == "attempted relative import with no known parent package"
    )
