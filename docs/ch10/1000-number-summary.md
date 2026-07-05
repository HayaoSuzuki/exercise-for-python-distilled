---
title: "1000: 数値列の要約"
description: "組み込み関数を使い、数値列の個数、合計、最小値、最大値を求めます。"
difficulty: 2
---

# 1000: 数値列の要約

## 問題

整数のイテラブル `values` を受け取り、個数、合計、最小値、最大値を辞書で返す関数 `summarize_numbers(values)` を実装してください。
返り値のキーは `"count"`、`"total"`、`"min"`、`"max"` とします。

## 制約

- `values` は整数のイテラブルです。
- 空の入力に対しては、個数と合計を `0`、最小値と最大値を `None` にします。
- イテレータを渡しても正しく動作するようにします。

## 例

```python
>>> summarize_numbers([])
{'count': 0, 'total': 0, 'min': None, 'max': None}
>>> summarize_numbers([3, 1, 4])
{'count': 3, 'total': 8, 'min': 1, 'max': 4}
>>> summarize_numbers(x for x in [10, -2, 5])
{'count': 3, 'total': 13, 'min': -2, 'max': 10}

```

## 発展

平均値も返すように拡張し、空の入力で平均値をどう表すかを決めてください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
