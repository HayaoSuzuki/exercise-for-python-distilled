"""0850: ミニ import システムと循環検出のリファレンス実装。"""


def load(
    name: str,
    deps: dict[str, list[str]],
    cache: dict[str, list[str]],
) -> list[str]:
    """モジュール name をロードし、新たにロードが完了したモジュール名を順に返す。

    cache は sys.modules 相当の辞書で、破壊的に更新する。
    未知のモジュールは ModuleNotFoundError、循環インポートは ImportError を送出する。
    """
    loaded: list[str] = []
    loading: list[str] = []  # ロード中（未完了）のモジュールのスタック

    def _load(modname: str) -> None:
        if modname in cache:
            return
        if modname in loading:
            cycle = [*loading[loading.index(modname) :], modname]
            raise ImportError("circular import: " + " -> ".join(cycle))
        if modname not in deps:
            raise ModuleNotFoundError(f"No module named {modname!r}")
        loading.append(modname)
        for dep in deps[modname]:
            _load(dep)
        loading.pop()
        cache[modname] = deps[modname]
        loaded.append(modname)

    _load(name)
    return loaded
