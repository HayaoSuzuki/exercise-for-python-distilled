---
title: "0903: 環境変数から探す Python ファイル"
description: "環境変数で指定されたディレクトリを pathlib で再帰的に調べ、Python ファイルの相対パスを返します。"
difficulty: 2
---

# 0903: 環境変数から探す Python ファイル

## 問題

環境変数名 `varname` を受け取り、その環境変数に入っているディレクトリ以下から Python ファイルを探す関数 `python_files_from_env(varname)` を実装してください。
返り値は、見つかった `.py` ファイルの相対パス文字列のリストです。

## 制約

- 環境変数の値は、探索を始めるディレクトリのパスです。
- サブディレクトリも再帰的に探索します。
- 返り値は、探索を始めたディレクトリからの相対パスです。
- パス区切り文字は `/` にそろえます。
- 返り値は辞書順に並べます。
- `.py` で終わる通常ファイルだけを返します。
- 環境変数が存在しない場合は `KeyError` を送出します。
- 環境変数が指すパスがディレクトリでない場合は `NotADirectoryError` を送出します。

## 例

```python
>>> import os
>>> from pathlib import Path
>>> from tempfile import TemporaryDirectory
>>> with TemporaryDirectory() as dirname:
...     root = Path(dirname)
...     (root / "pkg").mkdir()
...     _ = (root / "app.py").write_text("", encoding="utf-8")
...     _ = (root / "pkg" / "mod.py").write_text("", encoding="utf-8")
...     _ = (root / "notes.txt").write_text("", encoding="utf-8")
...     os.environ["PY_SOURCE_DIR"] = str(root)
...     python_files_from_env("PY_SOURCE_DIR")
['app.py', 'pkg/mod.py']

```

## 発展

拡張子を引数で指定できる版を書いてください。

## 参考

- 『Python Distilled』第9章「環境変数」
- 『Python Distilled』第9章「ディレクトリ」
- 『Python Distilled』第9章「I/O標準ライブラリ」
