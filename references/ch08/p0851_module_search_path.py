"""0851: モジュール検索パスの解決のリファレンス実装。"""


def find_module(name: str, path: list[str], vfs: dict[str, set[str]]) -> str:
    """path のディレクトリを順に探索し、最初に一致したモジュールのファイルパスを返す。

    同じディレクトリではパッケージ（__init__.py を持つディレクトリ）がモジュールより
    優先される。見つからなければ ModuleNotFoundError を送出する。
    """
    for directory in path:
        entries = vfs.get(directory, set())
        package_dir = f"{directory}/{name}"
        if name in entries and "__init__.py" in vfs.get(package_dir, set()):
            return f"{package_dir}/__init__.py"
        if f"{name}.py" in entries:
            return f"{directory}/{name}.py"
    raise ModuleNotFoundError(f"No module named {name!r}")
