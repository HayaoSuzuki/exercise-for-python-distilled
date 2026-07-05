"""0800: モジュールの公開名のリファレンス実装。"""

from collections.abc import Mapping


def exported_names(namespace: Mapping[str, object]) -> list[str]:
    """モジュール名前空間から公開名を返す。"""
    if "__all__" in namespace:
        all_value = namespace["__all__"]
        if not isinstance(all_value, (list, tuple)):
            raise TypeError("__all__ must be a list or tuple of strings")
        names: list[str] = []
        for name in all_value:
            if not isinstance(name, str):
                raise TypeError("__all__ must be a list or tuple of strings")
            names.append(name)
        return names
    return sorted(name for name in namespace if not name.startswith("_"))
