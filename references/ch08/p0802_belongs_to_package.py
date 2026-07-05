"""0802: パッケージに属するモジュール名のリファレンス実装。"""


def belongs_to_package(package: str, module: str) -> bool:
    """パッケージ自身またはそのサブモジュールかを返す。"""
    if package == "" or module == "":
        raise ValueError("names must be non-empty")
    return module == package or module.startswith(f"{package}.")

