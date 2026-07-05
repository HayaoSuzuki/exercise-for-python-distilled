---
title: "0754: 代数構造の抽象基底クラス"
description: "モノイドの抽象基底クラスと、繰り返し二乗法による O(log n) の冪演算ミックスインを実装します。"
difficulty: 4
---

# 0754: 代数構造の抽象基底クラス

## 問題

**モノイド**とは、集合 \(M\)、二項演算 \(\cdot : M \times M \to M\)、単位元 \(e \in M\) の組 \((M, \cdot, e)\) で、任意の \(x, y, z \in M\) について次の公理を満たすものです。

\[
(x \cdot y) \cdot z = x \cdot (y \cdot z), \qquad e \cdot x = x \cdot e = x
\]

整数の加法、文字列の連結、正方行列の乗法はいずれもモノイドです。
結合律があるため、冪 \(x^n\) は**繰り返し二乗法**によって \(O(\log n)\) 回の演算で計算できます。

モノイドのインタフェースを規定する抽象基底クラス `Monoid` を実装してください。

- `abc.ABC` を継承する。
- 抽象メソッド `op(a, b)`（二項演算）と `identity()`（単位元）を宣言する。
- 具象メソッド `power(x, n)` をミックスインとして提供する。`power(x, n)` は \(x\) を \(n\) 個 `op` で結合した値を返し、`power(x, 0)` は単位元を返す。

## 制約

- `n` は非負整数とします。負の場合は `ValueError` を送出します。
- `power(x, n)` の中での `op` の呼び出し回数は \(O(\log n)\) 回とします。`op` を \(n - 1\) 回呼ぶ素朴な反復は認めません（\(2 \lfloor \log_2 n \rfloor + 1\) 回以下に抑えられます）。
- 抽象メソッドを実装しない派生クラスがインスタンス化できないことは、`ABCMeta` の仕組みに任せてかまいません。
- `op` が結合律を満たすことは呼び出し側の責任とし、`power` の中で検査する必要はありません。

## 例

```python
>>> class Add(Monoid):
...     def op(self, a, b):
...         return a + b
...     def identity(self):
...         return 0
...
>>> Add().power(3, 10)
30
>>> Add().power(3, 0)
0
>>> class Concat(Monoid):
...     def op(self, a, b):
...         return a + b
...     def identity(self):
...         return ""
...
>>> Concat().power("ab", 3)
'ababab'
>>> class Mat2(Monoid):
...     def op(self, a, b):
...         (a11, a12), (a21, a22) = a
...         (b11, b12), (b21, b22) = b
...         return ((a11 * b11 + a12 * b21, a11 * b12 + a12 * b22),
...                 (a21 * b11 + a22 * b21, a21 * b12 + a22 * b22))
...     def identity(self):
...         return ((1, 0), (0, 1))
...
>>> Mat2().power(((1, 1), (1, 0)), 50)[0][1]  # フィボナッチ数 F(50)
12586269025

```

`op` の呼び出し回数が \(O(\log n)\) であることと、抽象基底クラスの働きも確認できます。

```python
>>> class CountingAdd(Add):
...     calls = 0
...     def op(self, a, b):
...         CountingAdd.calls += 1
...         return a + b
...
>>> CountingAdd().power(1, 10 ** 9)
1000000000
>>> CountingAdd.calls <= 60
True
>>> Monoid()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class Monoid without an implementation for abstract methods 'identity', 'op'
>>> Add().power(3, -1)
Traceback (most recent call last):
    ...
ValueError: n must be non-negative

```

## 発展

逆元を返す抽象メソッド `inv(x)` を追加した派生クラス `Group(Monoid)` を定義し、負の指数でも動くように `power` を拡張してください。

## 参考

- 『Python Distilled』第7章「型、インタフェース、抽象基底クラス」
- 『Python Distilled』第7章「多重継承、インタフェース、ミックスイン」
- [モノイド - Wikipedia](https://ja.wikipedia.org/wiki/モノイド)
- [Exponentiation by squaring - Wikipedia](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)
