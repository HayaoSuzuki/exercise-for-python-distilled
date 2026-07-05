import pytest

from references.ch08 import p0850_mini_import_system as import_mod


def test_load_returns_modules_completed_in_dependency_order() -> None:
    # Arrange
    deps = {"app": ["config", "utils"], "utils": ["config"], "config": []}
    cache: dict[str, list[str]] = {}

    # Act
    actual = import_mod.load("app", deps, cache)

    # Assert
    assert actual == ["config", "utils", "app"]


def test_load_returns_empty_list_for_cached_module() -> None:
    # Arrange
    deps = {"app": ["config"], "config": []}
    cache = {"config": []}

    # Act
    actual = import_mod.load("config", deps, cache)

    # Assert
    assert actual == []


def test_load_raises_module_not_found_for_missing_dependency() -> None:
    # Arrange
    deps = {"web": ["framework"]}
    cache: dict[str, list[str]] = {}

    # Act
    with pytest.raises(ModuleNotFoundError) as exc_info:
        import_mod.load("web", deps, cache)

    # Assert
    assert "No module named 'framework'" in str(exc_info.value)


def test_load_raises_import_error_for_cycle() -> None:
    # Arrange
    deps = {"moda": ["modb"], "modb": ["moda"]}
    cache: dict[str, list[str]] = {}

    # Act
    with pytest.raises(ImportError) as exc_info:
        import_mod.load("moda", deps, cache)

    # Assert
    assert "circular import: moda -> modb -> moda" in str(exc_info.value)
