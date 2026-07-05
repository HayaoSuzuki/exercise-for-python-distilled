---
title: "1004: zip と map の線形代数"
description: "タプルのタプルで表した行列に対する転置・積・累乗を zip、map、sum で組み立て、Fibonacci 数を対数時間で求めます。"
difficulty: 3
---

# 1004: zip と map の線形代数

## 問題

行列を「行のタプルを並べたタプル」で表します。
例えば \(2 \times 3\) 行列は `((1, 2, 3), (4, 5, 6))` です。
この表現に対して、次の関数を実装してください。

- `transpose(m)`：転置行列を返します。
- `mat_mul(a, b)`：行列の積 \(AB\) を返します。
- `mat_pow(m, n)`：正方行列の \(n\) 乗を返します。`n` が 0 のときは単位行列です。
- `fib(n)`：Fibonacci 数 \(F_n\)（\(F_0 = 0,\ F_1 = 1\)）を返します。

`fib` は恒等式

\[
\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^{n}
=
\begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}
\]

を使い、`mat_pow` の呼び出し1回で計算します。

## 制約

- 行列の要素は `int`、行列は空でないタプルのタプルです。
- 行列演算の内側のループは `zip`、`map`、`sum` を中心とした組み込み関数で書き、`m[i][j]` のような添字アクセスは使いません。
- `mat_mul(a, b)` は、`a` の列数と `b` の行数が一致しなければ `ValueError` を送出します。
- `mat_pow(m, n)` は、`m` が正方行列でなければ `ValueError` を、`n` が負の整数ならば `ValueError` を送出します。
- `mat_pow(m, n)` の行列乗算の回数は \(O(\log n)\) に抑えます。したがって `fib(n)` も \(O(\log n)\) 回の行列乗算で動きます。
- `fib(n)` の `n` が負ならば `ValueError` を送出します。

## 例

```python
>>> transpose(((1, 2, 3), (4, 5, 6)))
((1, 4), (2, 5), (3, 6))
>>> mat_mul(((1, 2), (3, 4)), ((5, 6), (7, 8)))
((19, 22), (43, 50))
>>> mat_mul(((1, 2, 3),), ((4,), (5,), (6,)))
((32,),)
>>> mat_pow(((1, 1), (1, 0)), 0)
((1, 0), (0, 1))
>>> mat_pow(((1, 1), (1, 0)), 10)
((89, 55), (55, 34))
>>> fib(0)
0
>>> fib(10)
55
>>> fib(100)
354224848179261915075
>>> mat_mul(((1, 2),), ((3, 4),))
Traceback (most recent call last):
  ...
ValueError: dimension mismatch: columns of a must equal rows of b
>>> mat_pow(((1, 2, 3), (4, 5, 6)), 2)
Traceback (most recent call last):
  ...
ValueError: m must be a square matrix

```

## 発展

トリボナッチ数列 \(T_n = T_{n-1} + T_{n-2} + T_{n-3}\)（\(T_0 = T_1 = 0,\ T_2 = 1\)）を \(3 \times 3\) 行列の累乗で表し、`mat_pow` をそのまま使って \(T_n\) を \(O(\log n)\) 回の行列乗算で求める関数 `tribonacci(n)` を書いてください。
一般に、\(k\) 項間の線形漸化式がどのような行列で表せるかも定式化してください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
- [フィボナッチ数 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%95%E3%82%A3%E3%83%9C%E3%83%8A%E3%83%83%E3%83%81%E6%95%B0)
