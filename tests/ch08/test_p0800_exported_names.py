import pytest

from references.ch08 import p0800_exported_names as names_mod


def test_exported_names_returns_sorted_public_names_without_all() -> None:
    # Arrange
    namespace = {"open": object(), "_helper": object(), "close": object()}

    # Act
    actual = names_mod.exported_names(namespace)

    # Assert
    assert actual == ["close", "open"]


def test_exported_names_uses_all_when_present() -> None:
    # Arrange
    namespace = {"__all__": ["run", "stop"], "run": object(), "_stop": object()}

    # Act
    actual = names_mod.exported_names(namespace)

    # Assert
    assert actual == ["run", "stop"]


@pytest.mark.parametrize("all_value", ["run", {"run"}, [1]])
def test_exported_names_rejects_invalid_all(all_value: object) -> None:
    # Arrange
    namespace = {"__all__": all_value}

    # Act
    with pytest.raises(TypeError) as exc_info:
        names_mod.exported_names(namespace)

    # Assert
    assert str(exc_info.value) == "__all__ must be a list or tuple of strings"
