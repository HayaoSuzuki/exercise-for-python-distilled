---
title: "0600: 累積和ジェネレータ"
description: "入力を1つずつ受け取り、その時点までの合計を順に生成します。"
difficulty: 2
---

# 0600: 累積和ジェネレータ

## 問題

整数のイテラブル `values` から累積和を順に生成するジェネレータ関数 `running_totals(values)` を実装してください。
各要素を読み取るたびに、その時点までの合計を `yield` します。

## 制約

- `values` は整数のイテラブルです。
- 空の入力に対しては何も生成しません。
- 入力全体をリストに変換する必要はありません。

## 例

```python
>>> list(running_totals([]))
[]
>>> list(running_totals([3, -1, 4]))
[3, 2, 6]
>>> list(running_totals(x for x in [1, 2, 3]))
[1, 3, 6]

```

## 発展

累積和が指定した上限を超えた時点で生成を止めるジェネレータを書いてください。

## 参考

- 『Python Distilled』第6章「ジェネレータとyield文」
- 『Python Distilled』第6章「再利用できるジェネレータ」
