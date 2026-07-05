---
title: "0800: モジュールの公開名"
description: "名前空間から、外部に公開する名前の一覧を求めます。"
difficulty: 2
---

# 0800: モジュールの公開名

## 問題

モジュールの名前空間を表す辞書 `namespace` から、外部に公開する名前を求める関数 `exported_names(namespace)` を実装してください。
`__all__` がある場合はその内容を公開名として使います。
`__all__` がない場合は、アンダースコアで始まらない名前を公開名とします。

## 制約

- `namespace` は文字列キーを持つマッピングです。
- `__all__` がある場合、その値は文字列だけを含む `list` または `tuple` とします。
- `__all__` がある場合は、そこに書かれた順序を保って返します。
- `__all__` がない場合は、公開名を辞書順に並べて返します。
- `__all__` の値が不正なときは `TypeError` を送出します。

## 例

```python
>>> exported_names({"open": object(), "_helper": object(), "close": object()})
['close', 'open']
>>> exported_names({"__all__": ["run", "stop"], "run": object(), "_stop": object()})
['run', 'stop']
>>> exported_names({"__all__": "run"})
Traceback (most recent call last):
    ...
TypeError: __all__ must be a list or tuple of strings

```

## 発展

`__all__` に存在しない名前が含まれている場合を検出し、例外として報告する仕様に拡張してください。

## 参考

- 『Python Distilled』第8章「モジュールから選んでインポートする」
- 『Python Distilled』第8章「パッケージにおける名前空間の制御」
- 『Python Distilled』第8章「公開するパッケージの制御」
