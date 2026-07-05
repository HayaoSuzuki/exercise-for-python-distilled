---
title: "0805: from module import * の意味論"
description: "from module import * が束縛する名前の集合を __all__ とアンダースコア規則から求めます。"
difficulty: 3
---

# 0805: `from module import *` の意味論

## 問題

`from module import *` が現在の名前空間に束縛する名前は、モジュールが `__all__` を定義しているかどうかで決まります。
この規則を、モジュールの名前空間を表す辞書に対する関数として実装します。

関数 `star_exports(namespace, all_names=None)` を実装してください。

- `namespace` はモジュールのグローバル名前空間を表す辞書です。
- 束縛される名前の集合（`set[str]`）を返します。

使う `__all__` は次の優先順位で決まります。

1. 引数 `all_names` が `None` でなければ、それを `__all__` として使う。
2. `all_names` が `None` で、`namespace` にキー `"__all__"` があれば、その値を使う。
3. どちらもなければ `__all__` は未定義とする。

`__all__` が定義されている場合は、その要素すべてからなる集合を返します。
`namespace` に存在しない名前が `__all__` に含まれていたら `AttributeError` を送出します（`__all__` の並びで最初に見つかった名前を報告します）。
メッセージは `module has no attribute 'x'` の形式です。

`__all__` が未定義の場合は、アンダースコアで始まらない名前すべての集合を返します
（`_helper` や `__name__` のような名前は束縛されません）。

## 制約

- `namespace` は `dict[str, object]`、`all_names` は `list[str] | None` です。
- `namespace` の `"__all__"` キーの値は `list[str]` とみなしてかまいません。
- `__all__` の要素に重複があってもかまいません（結果は集合なので 1 回だけ現れます）。

## 例

```python
>>> ns = {"__name__": "module", "a": 37, "func": 1, "SomeClass": 2, "_helper": 3}
>>> sorted(star_exports(ns))
['SomeClass', 'a', 'func']
>>> sorted(star_exports(ns, all_names=["func", "SomeClass"]))
['SomeClass', 'func']
>>> ns["__all__"] = ["func", "a", "func"]
>>> sorted(star_exports(ns))
['a', 'func']
>>> star_exports(ns, all_names=["func", "gone"])
Traceback (most recent call last):
  ...
AttributeError: module has no attribute 'gone'

```

## 発展

本章の「公開するパッケージの制御」で説明される `__all__` の伝播を実装してください。
サブモジュールの名前空間のリストを受け取り、各サブモジュールの `star_exports` の結果を合成して、`__init__.py` 相当の名前空間（持ち上げられた名前の束縛と、それらを連結した `__all__`）を返す関数を書きます。
同じ名前が複数のサブモジュールから公開されたら例外を送出します。

## 参考

- 『Python Distilled』第8章「モジュールから選んでインポートする」
- 『Python Distilled』第8章「公開するパッケージの制御」
