---
title: "0802: モジュール検索パスの解決"
description: "sys.path 相当の検索パスを順に探索する first-match のモジュール解決を実装します。"
difficulty: 3
---

# 0802: モジュール検索パスの解決

## 問題

`import` 文はモジュールのソースコードを `sys.path` のディレクトリから順に検索し、最初に見つかったものを採用します。
この first-match 規則により、検索パスの前方にある同名のモジュールが後方のモジュールを隠します（shadowing）。

この探索を仮想ファイルシステム上で行う関数 `find_module(name, path, vfs)` を実装してください。

- `vfs` は、ディレクトリの絶対パスから、そのディレクトリ直下のエントリ名の集合への辞書です。
- ディレクトリ `d` 直下のエントリ `e` がディレクトリであるとは、`f"{d}/{e}"` が `vfs` のキーであることをいいます。
  それ以外のエントリはファイルです。
- `path` は `sys.path` に相当するディレクトリパスのリストです。

探索は次の規則で行います。

1. `path` のディレクトリ `d` を先頭から順に調べる。
2. `d` 直下にディレクトリ `name` があり、その中にファイル `__init__.py` があれば、パッケージとして一致する。
   `f"{d}/{name}/__init__.py"` を返す。
3. そうでなく、`d` 直下にファイル `f"{name}.py"` があれば、モジュールとして一致する。
   `f"{d}/{name}.py"` を返す。
4. `__init__.py` を持たないディレクトリ `name` はパッケージとみなさず、無視して探索を続ける。

規則 2 を規則 3 より先に適用するため、同じディレクトリに `spam.py` とパッケージ `spam/` の両方がある場合はパッケージが選ばれます。

## 制約

- `name` はドットを含まない単純なモジュール名です。
- パスの区切り文字は常に `/` とします。
- `path` の要素が `vfs` のキーにない場合は、空のディレクトリとして扱います。
- どのディレクトリでも見つからない場合は `ModuleNotFoundError` を送出します。
  メッセージは `No module named 'x'` の形式です。
- 名前空間パッケージ（`__init__.py` のないディレクトリ）は扱いません。

## 例

```python
>>> vfs = {
...     "/usr/lib/python": {"math.py", "json.py"},
...     "/home/user/proj": {"math.py", "graphics", "data"},
...     "/home/user/proj/graphics": {"__init__.py", "lines.py"},
...     "/home/user/proj/data": {"records.csv"},
... }
>>> sys_path = ["/home/user/proj", "/usr/lib/python"]
>>> find_module("json", sys_path, vfs)
'/usr/lib/python/json.py'
>>> find_module("math", sys_path, vfs)
'/home/user/proj/math.py'
>>> find_module("graphics", sys_path, vfs)
'/home/user/proj/graphics/__init__.py'
>>> find_module("data", sys_path, vfs)
Traceback (most recent call last):
  ...
ModuleNotFoundError: No module named 'data'

```

同じディレクトリでは、パッケージがモジュールより優先されます。

```python
>>> vfs2 = {
...     "/site": {"spam.py", "spam"},
...     "/site/spam": {"__init__.py"},
... }
>>> find_module("spam", ["/site"], vfs2)
'/site/spam/__init__.py'

```

## 発展

ドット区切りの完全修飾名（例：`"graphics.lines"`）を受け取る `find_qualified(name, path, vfs)` に拡張してください。
先頭の要素を `path` から解決した後は、見つかったパッケージのディレクトリだけを起点として残りの要素を解決します。
どの要素で解決に失敗したかを例外メッセージで区別できるようにします。

## 参考

- 『Python Distilled』第8章「モジュールの検索パス」
- 『Python Distilled』第8章「パッケージ」
