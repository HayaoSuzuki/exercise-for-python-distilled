import pytest

from references.ch08 import p0802_belongs_to_package as package_mod


@pytest.mark.parametrize(
    ("package", "module"),
    [
        ("spam", "spam"),
        ("spam", "spam.eggs"),
    ],
)
def test_belongs_to_package_accepts_package_and_submodules(package: str, module: str) -> None:
    # Arrange

    # Act
    actual = package_mod.belongs_to_package(package, module)

    # Assert
    assert actual is True


@pytest.mark.parametrize(
    ("package", "module"),
    [
        ("spam", "spammer.eggs"),
        ("spam.eggs", "spam"),
    ],
)
def test_belongs_to_package_rejects_unrelated_names(package: str, module: str) -> None:
    # Arrange

    # Act
    actual = package_mod.belongs_to_package(package, module)

    # Assert
    assert actual is False


@pytest.mark.parametrize(("package", "module"), [("", "spam"), ("spam", "")])
def test_belongs_to_package_rejects_empty_names(package: str, module: str) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        package_mod.belongs_to_package(package, module)

    # Assert
    assert str(exc_info.value) == "names must be non-empty"
