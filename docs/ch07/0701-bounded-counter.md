---
title: "0701: 上限付きカウンタ"
description: "インスタンス属性、プロパティ、メソッドで値の範囲を保つクラスを作ります。"
difficulty: 2
---

# 0701: 上限付きカウンタ

## 問題

0 以上 `limit` 以下の値を持つクラス `BoundedCounter` を実装してください。
カウンタは値を増やしたり、0 に戻したりできます。

## 制約

- `BoundedCounter(limit, value=0)` でカウンタを作ります。
- `limit` が負のときは `ValueError` を送出します。
- 初期値 `value` が `0 <= value <= limit` を満たさないときは `ValueError` を送出します。
- `value` は読み取り専用のプロパティです。
- `increment(amount=1)` は正の整数を受け取り、値を増やして新しい値を返します。
- `increment()` の結果が `limit` を超えるときは `ValueError` を送出します。
- `reset()` は値を 0 に戻し、0 を返します。

## 例

```python
>>> counter = BoundedCounter(5, 2)
>>> counter.value
2
>>> counter.increment()
3
>>> counter.increment(2)
5
>>> counter.reset()
0
>>> BoundedCounter(2).increment(3)
Traceback (most recent call last):
    ...
ValueError: counter limit exceeded

```

## 発展

`decrement()` を追加し、値が 0 未満にならないようにしてください。

## 参考

- 『Python Distilled』第7章「class文」
- 『Python Distilled』第7章「インスタンス」
- 『Python Distilled』第7章「インスタンスの属性」
- 『Python Distilled』第7章「プロパティ」
