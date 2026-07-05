---
title: "1003: 安定ソートで作る基数ソート"
description: "sorted の安定性を桁ごとに積み重ねて、非負整数の LSD 基数ソートを実装します。"
difficulty: 3
---

# 1003: 安定ソートで作る基数ソート

## 問題

組み込み関数 `sorted` は**安定**です。
すなわち、キーが等しい要素どうしの相対順序を保ちます。
この性質を使うと、要素全体を一度に比較しなくても、下位の桁から順に「その桁だけをキーにした安定ソート」を繰り返すことで全体を整列できます。
これが LSD（least significant digit）方式の**基数ソート**であり、桁ごとの並べ替えをバケットへの振り分けで行えば、最大値の桁数を \(k\) として \(O(kn)\) で動きます。

関数 `radix_sort(nums, base=10)` を実装してください。
非負整数のリスト `nums` を昇順に並べた新しいリストを返します。
`base` は桁を取り出すときの基数です。

## 制約

- `nums` は非負整数のリストです。負の数が含まれていたら `ValueError` を送出します。
- `base` は2以上の整数です。そうでなければ `ValueError` を送出します。
- `sorted`（または `list.sort`）の呼び出しは、キー関数が特定の1桁の値（0 以上 `base` 未満の整数）を返す形に限ります。要素全体を一度に比較してはいけません。
- 引数のリスト `nums` を書き換えてはいけません。
- 空のリストには空のリストを返します。

## 例

```python
>>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
[2, 24, 45, 66, 75, 90, 170, 802]
>>> radix_sort([0, 10, 1, 100, 11])
[0, 1, 10, 11, 100]
>>> radix_sort([3, 1, 2], base=2)
[1, 2, 3]
>>> radix_sort([])
[]
>>> nums = [5, 3, 5, 1]
>>> radix_sort(nums)
[1, 3, 5, 5]
>>> nums
[5, 3, 5, 1]
>>> radix_sort([1, -2])
Traceback (most recent call last):
  ...
ValueError: all elements must be non-negative integers
>>> radix_sort([1, 2], base=1)
Traceback (most recent call last):
  ...
ValueError: base must be an integer >= 2

```

## 発展

比較に基づくソートには \(\Omega(n \log n)\) 回の比較が必要という下界が知られています。
一方、この演習の実装は桁ごとのパスに比較ソートである `sorted` を使うため、計算量は \(O(kn \log n)\) です。
桁ごとのパスを `sorted` の代わりにバケットへの振り分け（計数ソート）で書き直して \(O(kn)\) を達成し、それでも比較ソートの下界と矛盾しない理由を説明してください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
- [基数ソート - Wikipedia](https://ja.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E3%82%BD%E3%83%BC%E3%83%88)
- [比較ソート - Wikipedia](https://ja.wikipedia.org/wiki/%E6%AF%94%E8%BC%83%E3%82%BD%E3%83%BC%E3%83%88)
