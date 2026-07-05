---
title: "0205: ジェネレータ式と包除原理"
description: "与えられた素数のどれとも互いに素な整数の個数をジェネレータ式で数えます。"
difficulty: 3
---

# 0205: ジェネレータ式と包除原理

## 問題

相異なる素数の集まり \(P\) が与えられたとき、`count_coprimes(n, primes)` を実装してください。
返り値は 1 以上 \(n\) 以下の整数のうち、`primes` のどの素数でも割り切れないものの個数です。

この個数は包除原理により

\[
\#\{\, k \in \{1, \dots, n\} : \forall p \in P,\ p \nmid k \,\}
= \sum_{S \subseteq P} (-1)^{|S|} \left\lfloor \frac{n}{\prod_{p \in S} p} \right\rfloor
\]

と表せます。
特に \(P\) が \(n\) の素因数全体のとき、この値はオイラーのトーシェント関数 \(\varphi(n)\) に一致します。

関数本体は、`sum()` に渡す1つのジェネレータ式（`all()` または `any()` を併用）として書いてください。
上の式を直接計算する方針を取る場合は、`itertools.combinations` を使ってかまいません。

## 制約

- `n` は非負整数です。`n = 0` のときは 0 を返します。
- `primes` は相異なる素数のシーケンスです。空の場合は `n` を返します。要素が実際に素数であることの検証は不要です。
- 明示的な `for` 文・`while` 文を使わず、関数本体は単一の `return` 文で書いてください。
- \(n \le 10^6\)、\(|P| \le 10\) 程度の入力で数秒以内に動くこと。

## 例

```python
>>> count_coprimes(30, [2, 3, 5])
8
>>> count_coprimes(100, [2, 3, 5, 7])
22
>>> count_coprimes(10, [])
10
>>> count_coprimes(0, [2])
0
>>> count_coprimes(10**6, [2, 3, 5, 7, 11, 13])
191808

```

## 発展

- \(n = 10^{18}\) のような巨大な \(n\) でも即座に答えが出るよう、包除原理の式を `itertools.combinations` と `math.prod` で直接計算する実装に書き換えてください。和の項数は \(2^{|P|}\) 個で済みます。
- \(n\) の素因数の一覧 `factors` を受け取って \(\varphi(n)\) を返す `totient(n, factors)` を書き、`count_coprimes(n, factors)` と一致することを確かめてください。

## 参考

- 『Python Distilled』第2章「ジェネレータ式」
- 『Python Distilled』第2章「イテラブルオブジェクト」
- [包除原理 - Wikipedia](https://ja.wikipedia.org/wiki/包除原理)
