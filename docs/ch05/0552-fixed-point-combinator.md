---
title: "0552: 不動点コンビネータ"
description: "λ計算の Z コンビネータに倣い、名前による自己参照なしで再帰を実現する不動点コンビネータ fix を実装します。"
difficulty: 5
---

# 0552: 不動点コンビネータ

## 問題

再帰関数は、通常は関数本体から自分自身の名前を参照して定義します。
しかし、λ計算には名前付きの定義が存在しないため、無名関数だけで再帰を組み立てる方法が必要になります。
それが**不動点コンビネータ**で、高階関数 \(F\) に対して

\[
\mathrm{fix}\,F = F\,(\mathrm{fix}\,F)
\]

を満たす関数 \(\mathrm{fix}\,F\)（\(F\) の不動点）を返します。
値渡し（作用的順序）の言語では、次の Z コンビネータがその実装として知られています。

\[
Z = \lambda f.\,(\lambda x.\,f\,(\lambda v.\,x\,x\,v))\,(\lambda x.\,f\,(\lambda v.\,x\,x\,v))
\]

不動点コンビネータ `fix(f)` を実装してください。

- `f` は、再帰呼び出しに使う関数 `rec` を受け取って本体の関数を返す高階関数です。
- `fix(f)` は、本体の中の `rec(...)` が本体自身の呼び出しになるように結び付けた関数を返します。
- 次の形で使えることが仕様です。

```python
fact = fix(lambda rec: lambda n: 1 if n == 0 else n * rec(n - 1))

```

## 制約

- `fix` の実装の中で `fix` 自身の名前を参照してはいけません（名前による再帰の禁止）。
- `while` や `for` などのループで再帰を模倣してはいけません。
- 本体の関数は任意個の位置引数を取れるものとします。
- 再帰の深さは Python の再帰制限に収まる範囲とします。

## 例

```python
>>> fact = fix(lambda rec: lambda n: 1 if n == 0 else n * rec(n - 1))
>>> fact(0)
1
>>> fact(10)
3628800
>>> fib = fix(lambda rec: lambda n: n if n < 2 else rec(n - 1) + rec(n - 2))
>>> [fib(n) for n in range(10)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
>>> gcd = fix(lambda rec: lambda a, b: a if b == 0 else rec(b, a % b))
>>> gcd(1071, 462)
21

```

## 発展

Y コンビネータ \(Y = \lambda f.\,(\lambda x.\,f\,(x\,x))\,(\lambda x.\,f\,(x\,x))\) をそのまま Python に写すと、`fix` の呼び出しが停止しません。
値渡しの評価戦略の下でなぜ停止しないのか、Z コンビネータの \(\lambda v.\,x\,x\,v\)（η展開）がなぜそれを防ぐのかを説明してください。

## 参考

- 『Python Distilled』第5章「lambda式」
- 『Python Distilled』第5章「高階関数」
- 『Python Distilled』第5章「再帰」
- [不動点コンビネータ - Wikipedia](https://ja.wikipedia.org/wiki/不動点コンビネータ)
