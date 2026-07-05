import pytest

from references.ch09 import p0903_python_files_from_env as files_mod


def test_python_files_from_env_returns_relative_python_files(tmp_path, monkeypatch) -> None:
    # Arrange
    (tmp_path / "pkg").mkdir()
    (tmp_path / "app.py").write_text("", encoding="utf-8")
    (tmp_path / "pkg" / "mod.py").write_text("", encoding="utf-8")
    monkeypatch.setenv("PY_SOURCE_DIR", str(tmp_path))

    # Act
    actual = files_mod.python_files_from_env("PY_SOURCE_DIR")

    # Assert
    assert actual == ["app.py", "pkg/mod.py"]


def test_python_files_from_env_ignores_non_python_files(tmp_path, monkeypatch) -> None:
    # Arrange
    (tmp_path / "app.py").write_text("", encoding="utf-8")
    (tmp_path / "notes.txt").write_text("", encoding="utf-8")
    monkeypatch.setenv("PY_SOURCE_DIR", str(tmp_path))

    # Act
    actual = files_mod.python_files_from_env("PY_SOURCE_DIR")

    # Assert
    assert actual == ["app.py"]


def test_python_files_from_env_returns_sorted_paths(tmp_path, monkeypatch) -> None:
    # Arrange
    (tmp_path / "z.py").write_text("", encoding="utf-8")
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    monkeypatch.setenv("PY_SOURCE_DIR", str(tmp_path))

    # Act
    actual = files_mod.python_files_from_env("PY_SOURCE_DIR")

    # Assert
    assert actual == ["a.py", "z.py"]


def test_python_files_from_env_rejects_missing_environment_variable(monkeypatch) -> None:
    # Arrange
    monkeypatch.delenv("PY_SOURCE_DIR", raising=False)

    # Act
    with pytest.raises(KeyError) as exc_info:
        files_mod.python_files_from_env("PY_SOURCE_DIR")

    # Assert
    assert exc_info.value.args == ("PY_SOURCE_DIR",)


def test_python_files_from_env_rejects_non_directory_path(tmp_path, monkeypatch) -> None:
    # Arrange
    file_path = tmp_path / "app.py"
    file_path.write_text("", encoding="utf-8")
    monkeypatch.setenv("PY_SOURCE_DIR", str(file_path))

    # Act
    with pytest.raises(NotADirectoryError):
        files_mod.python_files_from_env("PY_SOURCE_DIR")

    # Assert

