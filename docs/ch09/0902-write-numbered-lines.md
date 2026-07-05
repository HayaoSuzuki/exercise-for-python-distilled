---
title: "0902: 行番号付き出力"
description: "ファイルオブジェクトへ、行番号を付けたテキストを書き出します。"
difficulty: 2
---

# 0902: 行番号付き出力

## 問題

文字列のイテラブル `lines` と書き込み用のファイルオブジェクト `output` を受け取り、各行に行番号を付けて書き出す関数 `write_numbered_lines(lines, output)` を実装してください。
行番号は1から始めます。

## 制約

- 各出力行は `番号: 内容` の形にします。
- 各出力行の末尾には改行を付けます。
- `lines` に含まれる文字列は、そのまま内容として使います。
- `output` は `write()` メソッドを持つファイル風オブジェクトです。
- 返り値は `None` です。

## 例

```python
>>> from io import StringIO
>>> out = StringIO()
>>> write_numbered_lines(["alpha", "beta"], out)
>>> out.getvalue()
'1: alpha\n2: beta\n'
>>> empty = StringIO()
>>> write_numbered_lines([], empty)
>>> empty.getvalue()
''

```

## 発展

行番号の開始値を引数で指定できる版を書いてください。

## 参考

- 『Python Distilled』第9章「ファイルとファイルオブジェクト」
- 『Python Distilled』第9章「print()関数」
