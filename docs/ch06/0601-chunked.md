---
title: "0601: 固定長に区切るジェネレータ"
description: "イテラブルから値を読み取り、指定した個数ごとのタプルを生成します。"
difficulty: 2
---

# 0601: 固定長に区切るジェネレータ

## 問題

イテラブル `values` を指定した個数ごとに区切るジェネレータ関数 `chunked(values, size)` を実装してください。
各チャンクはタプルとして生成します。

## 制約

- `size` は正の整数です。
- `size <= 0` のときは `ValueError` を送出します。
- 最後に余った要素が `size` 個未満でも、その要素からなるタプルを生成します。
- 入力全体をリストに変換する必要はありません。

## 例

```python
>>> list(chunked([], 3))
[]
>>> list(chunked([1, 2, 3, 4, 5], 2))
[(1, 2), (3, 4), (5,)]
>>> list(chunked((x for x in [1, 2, 3]), 2))
[(1, 2), (3,)]
>>> list(chunked([1], 0))
Traceback (most recent call last):
    ...
ValueError: size must be positive

```

## 発展

最後のチャンクが `size` 個に満たないときに捨てる版を書いてください。

## 参考

- 『Python Distilled』第6章「ジェネレータとyield文」
- 『Python Distilled』第6章「再利用できるジェネレータ」
