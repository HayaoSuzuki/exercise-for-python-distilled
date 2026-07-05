---
title: "0105: ニュートン法による整数平方根"
description: "整数演算だけのニュートン法で平方根の整数部分を求めます。"
difficulty: 3
---

# 0105: ニュートン法による整数平方根

## 問題

非負整数 \(n\) の**整数平方根**とは \(\lfloor \sqrt{n} \rfloor\)、すなわち \(x^2 \le n\) を満たす最大の整数 \(x\) です。
実数の世界では、方程式 \(x^2 - n = 0\) にニュートン法を適用すると反復式

\[
x_{k+1} = \frac{1}{2}\left(x_k + \frac{n}{x_k}\right)
\]

が得られ、\(\sqrt{n}\) に二次収束します。
この反復を整数の除算に置き換えても、適切な初期値と停止条件を選べば \(\lfloor \sqrt{n} \rfloor\) が正確に求められます。

関数 `isqrt(n)` を実装してください。
非負整数 `n` に対して \(\lfloor \sqrt{n} \rfloor\) を `int` で返します。
反復をどこで止めれば結果がちょうど \(\lfloor \sqrt{n} \rfloor\) になるのか、停止条件の正しさを説明できるようにしてください。

## 制約

- `n` は `int` です。負の場合は `ValueError` を送出します。
- 整数演算（四則演算、整数除算、比較）のみ使います。`math` モジュールは使いません。
- `float` への変換や `** 0.5` も使いません。\(n\) が \(10^{40}\) 程度でも正確な値を返す必要があります。
- 反復回数は \(n\) の桁数に対して高々多項式に収まるようにします。

## 例

```python
>>> isqrt(0)
0
>>> isqrt(1)
1
>>> isqrt(15)
3
>>> isqrt(16)
4
>>> isqrt(10**40)
100000000000000000000
>>> isqrt(10**40 - 1)
99999999999999999999
>>> isqrt(-1)
Traceback (most recent call last):
  ...
ValueError: isqrt() argument must be nonnegative

```

## 発展

同じ考え方で \(k\) 乗根の整数部分 \(\lfloor n^{1/k} \rfloor\) を返す関数 `iroot(n, k)` を実装してください。
また、`isqrt` の反復ごとの値を記録し、正しい桁数が反復のたびにほぼ倍増する（二次収束する）ことを大きな \(n\) で観察してください。

## 参考

- 『Python Distilled』第1章「算術演算子」
- 『Python Distilled』第1章「条件分岐と制御構造」
- 『Python Distilled』第1章「例外」
- [ニュートン法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%88%E3%83%B3%E6%B3%95)
