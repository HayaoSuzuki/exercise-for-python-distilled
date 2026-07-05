---
title: "0954: asyncio による有界並行実行"
description: "セマフォで同時実行数を制限しながらコルーチン群を並行実行し、結果を入力順で返します。"
difficulty: 5
---

# 0954: asyncio による有界並行実行

## 問題

多数の I/O タスク（HTTP リクエスト、DB クエリなど）を `asyncio.gather()` で一斉に起動すると、接続数やメモリの制約を超えてしまうことがあります。
このような場面では、**セマフォ**で同時実行数に上限を設ける方法がよく使われます。

次の非同期関数を実装してください。

```
async def gather_bounded(coros, limit):
    ...
```

- `coros` はコルーチンオブジェクト（awaitable）の反復可能オブジェクト、`limit` は同時実行数の上限です。
- すべてのコルーチンを実行し、結果を**入力と同じ順序**のリストで返します。
- どの時点でも、`await` の実行中にあるコルーチンは高々 `limit` 個に保ちます。制限には `asyncio.Semaphore` を使います。

「例」の後半では、実行中の個数を数えるカウンタで「同時実行数が上限を超えないこと」を検証しています。

## 制約

- `limit` が 1 未満の場合は `ValueError` を送出します（メッセージは「例」に合わせます）。
- `coros` が空の場合は空のリストを返します。
- 結果の順序は完了順ではなく入力順です。
- スレッドは使いません。`asyncio` の範囲で実装します。

## 例

```python
>>> import asyncio
>>> async def square(x):
...     await asyncio.sleep(0)
...     return x * x
>>> asyncio.run(gather_bounded([square(i) for i in range(5)], 2))
[0, 1, 4, 9, 16]
>>> asyncio.run(gather_bounded([], 3))
[]
>>> asyncio.run(gather_bounded([], 0))
Traceback (most recent call last):
    ...
ValueError: limit は 1 以上でなければなりません

```

同時実行数をカウンタで検証します。
`running` は実行中のコルーチンの個数、`peak` はその最大値です。

```python
>>> running = 0
>>> peak = 0
>>> async def tracked(x):
...     global running, peak
...     running += 1
...     peak = max(peak, running)
...     await asyncio.sleep(0.01)
...     running -= 1
...     return x
>>> asyncio.run(gather_bounded([tracked(i) for i in range(10)], 3))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> peak <= 3
True

```

## 発展

1 つのコルーチンが例外を送出すると `asyncio.gather()` の既定動作では他の結果も失われます。
例外を送出したタスクの結果として例外オブジェクトそのものを対応する位置に入れて返す `gather_bounded(coros, limit, return_exceptions=True)` を実装してください。
また、`asyncio.Semaphore` を使わずに、常に `limit` 個のワーカーがキューからコルーチンを取り出して実行する方式（ワーカープール）でも同じ仕様を実装し、両者の違い（起動されるタスク数など）を比較してください。

## 参考

- 『Python Distilled』第9章「ブロッキングと並行処理」の「asyncioによる並列処理」
- 『Python Distilled』第9章「I/O標準ライブラリ」の「`asyncio`」
- [asyncio synchronization primitives - Python 公式ドキュメント](https://docs.python.org/ja/3/library/asyncio-sync.html)
