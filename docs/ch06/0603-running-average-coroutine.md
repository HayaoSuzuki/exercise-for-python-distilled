---
title: "0603: send で更新する平均値"
description: "拡張ジェネレータに値を送り、送るたびに現在の平均を受け取ります。"
difficulty: 2
---

# 0603: send で更新する平均値

## 問題

値を `send()` で受け取り、これまでに受け取った数値の平均を返す拡張ジェネレータ `running_average()` を実装してください。

## 制約

- `running_average()` はジェネレータオブジェクトを返します。
- 最初の `next()` または `send(None)` は `None` を返し、値をまだ受け取っていない状態にします。
- 数値を `send(value)` すると、その値を含めた現在の平均を `float` で返します。
- 最初の値を受け取る前に値以外を `send()` するケースは扱わなくてかまいません。
- すでに値を受け取った後に `send(None)` された場合は、平均を変えずに現在の平均を返します。

## 例

```python
>>> avg = running_average()
>>> next(avg) is None
True
>>> avg.send(10.0)
10.0
>>> avg.send(20.0)
15.0
>>> avg.send(None)
15.0

```

## 発展

平均だけでなく、受け取った個数も返す版を書いてください。

## 参考

- 『Python Distilled』第6章「拡張ジェネレータとyield式」
- 『Python Distilled』第6章「拡張ジェネレータの応用」
