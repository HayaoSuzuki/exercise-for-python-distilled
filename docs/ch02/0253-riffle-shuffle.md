---
title: "0253: スライスで作る完全シャッフル"
description: "アウトシャッフルをスライスで実装し、デッキが元の並びに戻るまでの回数を求めます。"
difficulty: 4
---

# 0253: スライスで作る完全シャッフル

## 問題

完全なリフルシャッフル（ファロシャッフル）は、偶数枚のデッキをちょうど半分に分け、上半分と下半分から1枚ずつ交互に重ねる操作です。
先頭のカードが先頭に残る流儀をアウトシャッフルと呼びます。
例えば `[1, 2, 3, 4, 5, 6, 7, 8]` は `[1, 5, 2, 6, 3, 7, 4, 8]` になります。

次の2つの関数を実装してください。

- `riffle(deck)` — リスト `deck` にアウトシャッフルを1回適用した新しいリストを返します。
- `shuffle_order(n)` — `n` 枚のデッキが初めて元の並びに戻るまでに必要なアウトシャッフルの回数（1 以上の最小値）を返します。

52枚の標準的なデッキは、8回のアウトシャッフルで元の並びに戻ることが知られています。

## 制約

- `riffle` の `deck` は任意の要素のリストです。入力を変更してはいけません。空リストには空リストを返します。
- `deck` の長さが奇数の場合、`riffle` は `ValueError("deck length must be even")` を送出します。
- `riffle` の並べ替えはスライス（必要なら `zip()` も）で書き、明示的な `for` 文・`while` 文や要素位置の逐次計算を使わないでください。
- `shuffle_order` の `n` は 2 以上の偶数です。それ以外の整数には `ValueError` を送出します。`shuffle_order` の反復にはループを使ってかまいません。

## 例

```python
>>> riffle([1, 2, 3, 4, 5, 6, 7, 8])
[1, 5, 2, 6, 3, 7, 4, 8]
>>> riffle(["A", "B"])
['A', 'B']
>>> shuffle_order(2)
1
>>> shuffle_order(8)
3
>>> shuffle_order(52)
8
>>> riffle([1, 2, 3])
Traceback (most recent call last):
    ...
ValueError: deck length must be even

```

## 発展

- 位置 \(i\)（0 始まり）のカードがアウトシャッフルで位置 \(2i \bmod (n - 1)\) に移ること（末尾のカードを除く）を示し、`shuffle_order(n)` が \(2\) の \(n - 1\) を法とする乗法的位数に等しいことを証明してください。この事実を使い、シャッフルを繰り返さずに位数を計算する実装に書き換えてください。
- 先頭のカードが2枚目に潜り込むインシャッフルを行う `riffle_in(deck)` と、その位数を返す `shuffle_order_in(n)` を実装してください。`shuffle_order_in(52)` はいくつになるでしょうか。

## 参考

- 『Python Distilled』第2章「シーケンス」
- 『Python Distilled』第2章「ミュータブルシーケンス」
- [Faro shuffle - Wikipedia](https://en.wikipedia.org/wiki/Faro_shuffle)
