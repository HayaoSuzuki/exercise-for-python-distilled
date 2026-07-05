"""0801: モジュール名からファイル名を作るリファレンス実装。"""

from keyword import iskeyword


def module_filename(name: str) -> str:
    """ドット区切りのモジュール名を相対的な Python ファイル名へ変換する。"""
    parts = name.split(".")
    if any(not part.isidentifier() or iskeyword(part) for part in parts):
        raise ValueError("invalid module name")
    return "/".join(parts) + ".py"
