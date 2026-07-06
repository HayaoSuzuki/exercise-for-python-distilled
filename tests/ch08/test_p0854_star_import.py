import pytest

from references.ch08 import p0854_star_import as star_mod


def test_star_exports_returns_public_names_without_all() -> None:
    # Arrange
    namespace = {"__name__": "module", "a": 37, "_helper": 3, "func": object()}

    # Act
    actual = star_mod.star_exports(namespace)

    # Assert
    assert actual == {"a", "func"}


def test_star_exports_uses_dunder_all_from_namespace() -> None:
    # Arrange
    namespace: dict[str, object] = {"__all__": ["a", "c"], "a": 1, "b": 2, "c": 3}

    # Act
    actual = star_mod.star_exports(namespace)

    # Assert
    assert actual == {"a", "c"}


def test_star_exports_uses_explicit_all_names() -> None:
    # Arrange
    namespace = {"__name__": "module", "a": 37, "func": object()}

    # Act
    actual = star_mod.star_exports(namespace, ["func"])

    # Assert
    assert actual == {"func"}


def test_star_exports_rejects_missing_name_from_all() -> None:
    # Arrange
    namespace: dict[str, object] = {"a": 1}
    names = ["gone"]

    # Act
    with pytest.raises(AttributeError) as exc_info:
        star_mod.star_exports(namespace, names)

    # Assert
    assert "gone" in str(exc_info.value)
