---
title: "0801: モジュール名からファイル名を作る"
description: "ドット区切りのモジュール名を、相対的な Python ファイル名へ変換します。"
difficulty: 2
---

# 0801: モジュール名からファイル名を作る

## 問題

ドット区切りのモジュール名 `name` を、相対的な Python ファイル名へ変換する関数 `module_filename(name: str) -> str` を実装してください。
たとえば、`"pkg.tools.reader"` は `"pkg/tools/reader.py"` に変換します。

## 制約

- `name` は文字列です。
- モジュール名の各要素は Python の識別子でなければなりません。
- 空の要素を含む名前に対しては `ValueError` を送出します。
- Python のキーワードを要素に含む名前に対しては `ValueError` を送出します。
- 区切り文字には `/` を使います。

## 例

```python
>>> module_filename("spam")
'spam.py'
>>> module_filename("pkg.tools.reader")
'pkg/tools/reader.py'
>>> module_filename("pkg..reader")
Traceback (most recent call last):
    ...
ValueError: invalid module name
>>> module_filename("class")
Traceback (most recent call last):
    ...
ValueError: invalid module name

```

## 発展

ファイル名ではなくパッケージの `__init__.py` を指す版を追加してください。

## 参考

- 『Python Distilled』第8章「モジュールとimport文」
- 『Python Distilled』第8章「パッケージ」
- 『Python Distilled』第8章「パッケージ内のインポート」
