---
title: "0801: ミニ import システムと循環検出"
description: "sys.modules 相当のキャッシュを持つミニ import システムを実装し、循環インポートを検出します。"
difficulty: 4
---

# 0801: ミニ import システムと循環検出

## 問題

Python の `import` 文は `sys.modules` というキャッシュ辞書を参照し、ロード済みのモジュールを再ロードしません。
この仕組みを単純化したミニ import システムを実装します。

関数 `load(name, deps, cache)` を実装してください。

- `deps` は、モジュール名から、そのモジュールが本体の先頭でインポートするモジュール名のリストへの辞書です。
- `cache` は `sys.modules` に相当する辞書で、`load` が破壊的に更新します。
- モジュールのロードは、依存モジュールをリスト順にすべてロードし終えたときに完了します。
  完了したモジュールは `cache` に登録します（キーはモジュール名、値はそのモジュールの依存リスト）。
- `cache` に登録済みのモジュールはロードしません。
  キャッシュの確認は `deps` の確認より先に行います（登録済みモジュールは `deps` に存在しなくてもかまいません）。
- 戻り値は、今回の呼び出しで新たにロードが完了したモジュール名を、完了した順に並べたリストです。

ロード中（ロードを開始したがまだ完了していない）のモジュールを再びロードしようとしたら、循環インポートとして `ImportError` を送出します。
メッセージは `circular import: ` に、循環路上のモジュール名を ` -> ` で連結したものを続けます。
循環路は最初に再訪されたモジュールから始まり、同じモジュール名で終わります。

## 制約

- `deps` と `cache` は `dict[str, list[str]]`、モジュール名は空でない文字列です。
- ロードしようとしたモジュールが `cache` にも `deps` にもない場合は、`ModuleNotFoundError` を送出します。
  メッセージは `No module named 'x'` の形式です。
- 循環インポートの場合は、上記の形式のメッセージを持つ `ImportError` を送出します。
- モジュール数と依存関係の総数は高々 \(10^3\) とします。

## 例

```python
>>> deps = {
...     "app": ["config", "utils"],
...     "utils": ["config"],
...     "config": [],
... }
>>> cache = {}
>>> load("app", deps, cache)
['config', 'utils', 'app']
>>> load("utils", deps, cache)
[]
>>> sorted(cache)
['app', 'config', 'utils']
>>> load("web", {"web": ["framework"]}, {})
Traceback (most recent call last):
  ...
ModuleNotFoundError: No module named 'framework'
>>> load("moda", {"moda": ["modb"], "modb": ["base", "moda"], "base": []}, {})
Traceback (most recent call last):
  ...
ImportError: circular import: moda -> modb -> moda

```

## 発展

実際の CPython は循環インポートで例外を送出しません。
モジュールの実行を開始した時点で部分初期化状態のモジュールを `sys.modules` に登録し、循環先の `import` はその部分初期化状態のモジュールで満たされます。
`load` をこの意味論に書き換え、本章の `moda` と `modb` の例で起きる「インポート順序によって成否が変わる」現象を再現してください。

## 参考

- 『Python Distilled』第8章「モジュールのキャッシュ」
- 『Python Distilled』第8章「循環インポート」
