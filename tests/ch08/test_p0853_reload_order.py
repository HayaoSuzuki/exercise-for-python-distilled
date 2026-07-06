import pytest

from references.ch08 import p0853_reload_order as reload_mod


def test_reload_order_returns_dependencies_before_dependents() -> None:
    # Arrange
    deps = {"web": ["app", "config"], "app": ["config"]}

    # Act
    actual = reload_mod.reload_order(deps)

    # Assert
    assert actual == ["config", "app", "web"]


def test_reload_order_counts_each_independent_dependency() -> None:
    # Arrange
    deps = {"release": ["x", "y", "z"]}

    # Act
    actual = reload_mod.reload_order(deps)

    # Assert
    assert actual == ["x", "y", "z", "release"]


def test_reload_order_ignores_duplicate_dependency_entries() -> None:
    # Arrange
    deps = {"app": ["config", "config"]}

    # Act
    actual = reload_mod.reload_order(deps)

    # Assert
    assert actual == ["config", "app"]


def test_reload_order_rejects_dependency_cycle() -> None:
    # Arrange
    deps = {"moda": ["modb"], "modb": ["moda"]}

    # Act
    with pytest.raises(ValueError) as exc_info:
        reload_mod.reload_order(deps)

    # Assert
    assert str(exc_info.value) == "dependency cycle detected"
