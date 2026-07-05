---
title: "0504: トランポリンと継続渡し形式"
description: "サンクを返す関数をループで駆動するトランポリンを実装し、再帰制限を超える深さの計算を実行します。"
difficulty: 5
---

# 0504: トランポリンと継続渡し形式

## 問題

Python の再帰呼び出しの深さには上限があり、現在の値は `sys.getrecursionlimit()` で確認できます（デフォルトは 1000）。
末尾呼び出し最適化を行う言語では末尾再帰はループと同等に実行されますが、Python は末尾呼び出し最適化を行わないため、上限を超える深さの再帰はそのまま `RecursionError` になります。

**トランポリン**はこの制限を回避する技法です。
関数は再帰呼び出しを直接行う代わりに、続きの計算を引数なしの callable（**サンク**）に包んで返します。
トランポリンは、受け取ったサンクを引数なしで呼び出す操作をループで繰り返し、サンクでない値が返ってきたらそれを最終結果とします。
呼び出しのネストがループに置き換わるため、スタックは深くなりません。

`trampoline(f, *args)` を実装してください。

- まず `f(*args)` を呼び出します。
- 返り値が callable である限り、それをサンクとみなして引数なしで呼び出し続けます。
- callable でない値が得られたら、それを返します。

## 制約

- `f` とサンクの返り値は、次のサンク（引数なしの callable）か、最終結果（callable でない値）のいずれかとします。
- 計算の最終結果が callable になるケースは扱いません。
- `sys.setrecursionlimit()` による再帰制限の変更は禁止します。
- `trampoline` 自身は再帰せず、ループで駆動します。

## 例

```python
>>> import sys
>>> def sum_to(n, acc=0):
...     if n == 0:
...         return acc
...     return lambda: sum_to(n - 1, acc + n)  # 再帰呼び出しをサンクに包んで返す
>>> trampoline(sum_to, 10)
55
>>> n = sys.getrecursionlimit() * 100
>>> trampoline(sum_to, n) == n * (n + 1) // 2  # 再帰制限の 100 倍の深さでも計算できる
True

```

**継続渡し形式**（CPS）と組み合わせると、末尾位置にない再帰呼び出しも扱えます。
階乗の `n * rec(n - 1)` は末尾呼び出しではありませんが、残りの計算を継続 `k` として引数に渡す形に変換すれば、すべての呼び出しが末尾位置に移ります。

```python
>>> import math
>>> def fact_cps(n, k=lambda v: v):
...     if n == 0:
...         return lambda: k(1)
...     return lambda: fact_cps(n - 1, lambda v: lambda: k(n * v))
>>> trampoline(fact_cps, 10)
3628800
>>> trampoline(fact_cps, 5000) == math.factorial(5000)
True

```

## 発展

二分木のノード値の総和を計算する関数を CPS に変換し、`trampoline` と組み合わせて、深さが再帰制限を超える線形の木（リスト状に退化した木）でも計算できるようにしてください。

## 参考

- 『Python Distilled』第5章「再帰」
- 『Python Distilled』第5章「高階関数」
- [トランポリン（計算機科学） - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%88%E3%83%A9%E3%83%B3%E3%83%9D%E3%83%AA%E3%83%B3_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%A6))
- [継続渡しスタイル - Wikipedia](https://ja.wikipedia.org/wiki/継続渡しスタイル)
