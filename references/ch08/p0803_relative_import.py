"""0803: 相対インポートの解決のリファレンス実装。"""


def resolve_name(name: str, package: str, level: int) -> str:
    """相対インポートを PEP 328 の規則に従って絶対モジュール名へ変換する。

    level 個のピリオドは package の階層を level - 1 段さかのぼることを意味する。
    さかのぼりが階層を超える場合や package が空の場合は ImportError を送出する。
    """
    if level < 1:
        raise ValueError("level must be at least 1")
    if not package:
        raise ImportError("attempted relative import with no known parent package")
    bits = package.rsplit(".", level - 1)
    if len(bits) < level:
        raise ImportError("attempted relative import beyond top-level package")
    base = bits[0]
    return f"{base}.{name}" if name else base
