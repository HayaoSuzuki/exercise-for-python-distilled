from references.ch08 import p0802_module_search_path as path_mod


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
