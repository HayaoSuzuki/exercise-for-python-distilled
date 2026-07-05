---
title: "1002: zip で作る隣接差"
description: "隣り合う数値の差を、zip とスライスを使ってリストにします。"
difficulty: 2
---

# 1002: zip で作る隣接差

## 問題

整数のシーケンス `values` を受け取り、隣り合う要素の差をリストで返す関数 `adjacent_differences(values)` を実装してください。
各差は、後ろの値から前の値を引いた値です。

## 制約

- 返り値の長さは `max(len(values) - 1, 0)` です。
- `values` の長さが0または1なら空リストを返します。
- `values` は変更してはいけません。

## 例

```python
>>> adjacent_differences([10, 13, 9, 9])
[3, -4, 0]
>>> adjacent_differences([5])
[]
>>> adjacent_differences((1, 4, 10))
[3, 6]

```

## 発展

隣り合う値を任意の2引数関数で畳み込む版を書いてください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
