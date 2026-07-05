import pytest

from references.ch08 import p0804_reload_order as reload_mod


def test_reload_order_returns_dependencies_before_dependents() -> None:
    # Arrange
    deps = {"web": ["app", "config"], "app": ["config"]}

    # Act
    actual = reload_mod.reload_order(deps)

    # Assert
    assert actual == ["config", "app", "web"]


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
    assert "dependency cycle detected" in str(exc_info.value)
