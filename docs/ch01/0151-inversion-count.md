---
title: "0151: 転倒数"
description: "列の乱れ具合を測る転倒数を、分割統治で O(n log n) 時間で数えます。"
difficulty: 3
---

# 0151: 転倒数

## 問題

列 \(a_0, a_1, \ldots, a_{n-1}\) の**転倒数**（inversion count）とは、\(i < j\) かつ \(a_i > a_j\) を満たす添字の組 \((i, j)\) の個数です。
転倒数は列がソート済みの状態からどれだけ乱れているかを測る量で、昇順の列で 0、降順の列で最大値 \(n(n-1)/2\) をとります。

関数 `count_inversions(seq)` を実装してください。
整数の列 `seq` の転倒数を `int` で返します。

## 制約

- `seq` は整数の列（`list` など）で、要素数は最大 \(10^5\) です。
- すべての組を数え上げる \(O(n^2)\) の解法は、この入力規模では採用しません。\(O(n \log n)\) 時間で実装してください。
- 等しい値の組（`seq[i] == seq[j]`）は転倒に数えません。
- 呼び出し後も `seq` の並びが変わらないようにします。

## 例

```python
>>> count_inversions([3, 1, 4, 1, 5])
3
>>> count_inversions([])
0
>>> count_inversions([1, 2, 3])
0
>>> count_inversions([5, 4, 3, 2, 1])
10
>>> count_inversions([2, 2, 1])
2
>>> count_inversions(list(range(100000, 0, -1)))
4999950000

```

## 発展

転倒数の合計だけでなく、各添字 \(j\) について「\(j\) より前にあって \(a_j\) より大きい要素の個数」を並べたリストを返す関数を書いてください。
また、マージソートに基づく解法とは別に、Binary Indexed Tree（Fenwick tree）を使った解法も実装し、両者の結果が一致することを確かめてください。

## 参考

- 『Python Distilled』第1章「リスト」
- 『Python Distilled』第1章「関数」
- [Inversion (discrete mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics))
