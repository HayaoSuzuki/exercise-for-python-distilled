import pytest

from references.ch08 import p0851_module_search_path as path_mod


def test_find_module_uses_first_matching_path_entry() -> None:
    # Arrange
    vfs = {"/usr/lib/python": {"json.py"}, "/home/user/proj": {"json.py"}}

    # Act
    actual = path_mod.find_module("json", ["/home/user/proj", "/usr/lib/python"], vfs)

    # Assert
    assert actual == "/home/user/proj/json.py"


def test_find_module_prefers_package_over_module_in_same_directory() -> None:
    # Arrange
    vfs = {"/site": {"spam.py", "spam"}, "/site/spam": {"__init__.py"}}

    # Act
    actual = path_mod.find_module("spam", ["/site"], vfs)

    # Assert
    assert actual == "/site/spam/__init__.py"


def test_find_module_skips_directory_missing_from_vfs() -> None:
    # Arrange
    vfs = {"/usr/lib/python": {"json.py"}}

    # Act
    actual = path_mod.find_module("json", ["/missing", "/usr/lib/python"], vfs)

    # Assert
    assert actual == "/usr/lib/python/json.py"


def test_find_module_does_not_treat_sibling_package_as_match() -> None:
    # Arrange
    vfs = {"/site": {"other.py"}, "/site/spam": {"__init__.py"}}

    # Act
    with pytest.raises(ModuleNotFoundError) as exc_info:
        path_mod.find_module("spam", ["/site"], vfs)

    # Assert
    assert str(exc_info.value) == "No module named 'spam'"


def test_find_module_falls_back_to_module_file_without_package_dir_entry() -> None:
    # Arrange
    vfs = {"/site": {"spam", "spam.py"}}

    # Act
    actual = path_mod.find_module("spam", ["/site"], vfs)

    # Assert
    assert actual == "/site/spam.py"


def test_find_module_raises_module_not_found_when_absent() -> None:
    # Arrange
    vfs: dict[str, set[str]] = {"/site": set()}

    # Act
    with pytest.raises(ModuleNotFoundError) as exc_info:
        path_mod.find_module("spam", ["/site"], vfs)

    # Assert
    assert str(exc_info.value) == "No module named 'spam'"
