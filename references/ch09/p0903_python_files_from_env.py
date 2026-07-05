"""0903: 環境変数から探す Python ファイルのリファレンス実装。"""

import os
from pathlib import Path


def python_files_from_env(varname: str) -> list[str]:
    root = Path(os.environ[varname])
    if not root.is_dir():
        raise NotADirectoryError(str(root))
    return sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*.py")
        if path.is_file()
    )

