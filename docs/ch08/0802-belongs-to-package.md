---
title: "0802: パッケージに属するモジュール名"
description: "ドット区切りの名前から、モジュールが指定したパッケージに属するかを判定します。"
difficulty: 2
---

# 0802: パッケージに属するモジュール名

## 問題

パッケージ名 `package` とモジュール名 `module` を受け取り、`module` が `package` に属するかを判定する関数 `belongs_to_package(package, module)` を実装してください。
ここでは、名前はドットで区切られた文字列として扱います。

## 制約

- `module` が `package` と同じ名前なら `True` を返します。
- `module` が `package + "."` で始まるなら `True` を返します。
- たまたま同じ接頭辞を持つだけの名前は `False` とします。
- `package` または `module` が空文字列なら `ValueError` を送出します。
- `ValueError` のメッセージは `names must be non-empty` とします。

## 例

```python
>>> belongs_to_package("spam", "spam")
True
>>> belongs_to_package("spam", "spam.eggs")
True
>>> belongs_to_package("spam", "spammer.eggs")
False
>>> belongs_to_package("", "spam")
Traceback (most recent call last):
    ...
ValueError: names must be non-empty

```

## 発展

相対インポートの `level` と現在のパッケージ名から、絶対モジュール名を作る関数を書いてください。

## 参考

- 『Python Distilled』第8章「モジュールとimport文」
- 『Python Distilled』第8章「パッケージ」
- 『Python Distilled』第8章「パッケージ内のインポート」
