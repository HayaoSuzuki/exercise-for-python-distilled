---
title: "0303: トランザクションを実現するコンテキストマネージャ"
description: "辞書への一連の変更を、例外発生時にまとめて巻き戻すコンテキストマネージャを実装します。"
difficulty: 3
---

# 0303: トランザクションを実現するコンテキストマネージャ

## 問題

データベースのトランザクションは、一連の更新を「すべて反映されるか、まったく反映されないか」のどちらかにします（ACID 特性の原子性）。
同じ性質を、辞書への更新に対してコンテキストマネージャで実現します。

クラス `transaction` を実装してください。

- `transaction(mapping)`: トランザクションの対象とする辞書 `mapping` を受け取ります。
- `__enter__()`: 辞書の現在の内容のスナップショットを取り、辞書自身を返します。
- `__exit__()`: `with` ブロックを正常に抜けた場合は変更をそのまま残します（コミット）。例外で抜けた場合は辞書の内容をスナップショット時点に巻き戻した上で（ロールバック）、その例外を `with` 文の外へ伝播させます。

## 制約

- 対象は `dict` 型のオブジェクトです。`with` ブロック内では、キーの追加、値の上書き、キーの削除を自由に行えます。
- 例外発生時は、辞書のキーと値の組を `__enter__()` 時点の状態に戻してください。
- `__exit__()` で例外を握りつぶしてはいけません。発生した例外はそのまま `with` 文の外へ伝播させてください。
- スナップショットは浅いコピーでかまいません。値として保持されるオブジェクトの内部状態までは巻き戻さなくてよいです。

## 例

```python
>>> config = {"host": "localhost", "port": 8080}
>>> with transaction(config) as t:
...     t["port"] = 80
...     t["debug"] = True
>>> config == {"host": "localhost", "port": 80, "debug": True}
True
>>> try:
...     with transaction(config) as t:
...         t["debug"] = False
...         del t["host"]
...         raise RuntimeError("rollback")
... except RuntimeError as e:
...     print(e)
rollback
>>> config == {"host": "localhost", "port": 80, "debug": True}
True

```

## 発展

`contextlib.contextmanager` デコレータを使い、同じ振る舞いをジェネレータ関数として書き直してください。
また、`with transaction(d)` を入れ子にした場合に、内側のロールバックが内側のスナップショット時点までしか巻き戻さないことを確認してください。

## 参考

- 『Python Distilled』第3章「コンテキストマネージャとwith文」
- [ACID（コンピュータ科学） - Wikipedia](https://ja.wikipedia.org/wiki/ACID_(コンピュータ科学))
