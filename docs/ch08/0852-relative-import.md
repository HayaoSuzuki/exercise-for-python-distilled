---
title: "0852: 相対インポートの解決"
description: "相対インポートを PEP 328 の規則に従って絶対モジュール名へ変換します。"
difficulty: 3
---

# 0852: 相対インポートの解決

## 問題

パッケージ内では `from ..primitive import lines` のような相対インポートが使えます。
相対名から絶対名への変換規則は PEP 328 で定められており、変換はパッケージ名の文字列操作だけで完結します。

関数 `resolve_name(name, package, level)` を実装してください。

- `name` は、`from` と `import` の間に書かれたモジュール名から先頭のピリオドを除いた部分です。
  `from . import lines` のようにピリオドだけの場合は空文字列です。
- `package` は、インポートを実行するモジュールが属するパッケージの絶対名です
  （モジュール `graphics.graph2d.plot2d` の中なら `"graphics.graph2d"`）。
- `level` は先頭のピリオドの個数です（`from .` なら 1、`from ..` なら 2）。

変換は次の規則で行います。

- level 個のピリオドは、`package` の階層を level - 1 段さかのぼることを意味する。
- さかのぼった先のパッケージ名に `name` をピリオドで連結した絶対名を返す。
  `name` が空文字列なら、さかのぼった先のパッケージ名そのものを返す。

## 制約

- `name` と `package` は、ピリオド区切りの識別子からなる文字列です。
- `level` は整数です。
  1 未満なら `ValueError` を送出します。
- `package` が空文字列（トップレベルモジュール）なら `ImportError` を送出します。
  メッセージは `attempted relative import with no known parent package` です。
- さかのぼりが `package` の階層を超える場合は `ImportError` を送出します。
  メッセージは `attempted relative import beyond top-level package` です。

## 例

```python
>>> resolve_name("primitive", "graphics.graph2d", 2)
'graphics.primitive'
>>> resolve_name("lines", "graphics.primitive", 1)
'graphics.primitive.lines'
>>> resolve_name("", "graphics.primitive", 1)
'graphics.primitive'
>>> resolve_name("primitive.lines", "graphics.graph2d", 2)
'graphics.primitive.lines'
>>> resolve_name("fill", "graphics", 2)
Traceback (most recent call last):
  ...
ImportError: attempted relative import beyond top-level package
>>> resolve_name("lines", "", 1)
Traceback (most recent call last):
  ...
ImportError: attempted relative import with no known parent package

```

## 発展

`"from ..primitive import lines, text"` のような `from` 文の文字列と `package` を受け取り、（絶対モジュール名、束縛される名前のリスト）の組を返す関数に拡張してください。
本章で構文エラーとされている形（`import .lines` や `from .. import primitive.lines`）は `SyntaxError` として拒否します。

## 参考

- 『Python Distilled』第8章「パッケージ内のインポート」
- [PEP 328 – Imports: Multi-Line and Absolute/Relative](https://peps.python.org/pep-0328/)
