---
title: "1001: 上位の点数"
description: "組み込み関数 sorted を使い、点数の高い項目を取り出します。"
difficulty: 2
---

# 1001: 上位の点数

## 問題

名前から点数への辞書 `scores` から、点数の高い順に上位 `n` 件を返す関数 `top_scores(scores: dict[str, int], n: int) -> list[tuple[str, int]]` を実装してください。
点数が同じ場合は名前の辞書順で並べます。

## 制約

- `scores` のキーは名前、値は点数です。
- `n <= 0` のときは空のリストを返します。
- `n` が項目数より大きいときは、すべての項目を返します。
- 入力の辞書を変更してはいけません。

## 例

```python
>>> top_scores({}, 3)
[]
>>> top_scores({"Ada": 10, "Grace": 12, "Alan": 12}, 2)
[('Alan', 12), ('Grace', 12)]
>>> top_scores({"Ada": 10, "Grace": 7}, 10)
[('Ada', 10), ('Grace', 7)]
>>> top_scores({"Ada": 10}, 0)
[]

```

## 発展

順位も含めたタプル `(rank, name, score)` を返す版を書いてください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
