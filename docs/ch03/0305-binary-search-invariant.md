---
title: "0305: 不変条件を assert する二分探索"
description: "ループ不変条件を assert 文で表明しながら、二分探索 bisect_left を実装します。"
difficulty: 3
---

# 0305: 不変条件を assert する二分探索

## 問題

`assert` 文は、その地点で常に真であるべき条件を表明するための文です。
表明が偽になったら、それはユーザの入力ミスではなくプログラムのバグを意味します。
この問題では、二分探索のループ不変条件を `assert` 文でコードに書き込みます。

関数 `bisect_left(a: list[int], x: int) -> int` を実装してください。
昇順にソートされたリスト `a` に対して、`x` を挿入してもソート順が保たれる最も左の位置 \(k\) を返します。
\(n = \mathrm{len}(a)\) として、返り値 \(k\) は次を満たします。

\[
\forall i \in [0, k):\ a[i] < x
\quad\text{かつ}\quad
\forall j \in [k, n):\ a[j] \ge x
\]

実装は、探索範囲を表す2つの添字 `lo`、`hi` を狭めていく反復版の二分探索とし、ループの各周回の先頭で次のループ不変条件を `assert` 文で表明してください。

\[
0 \le \mathit{lo} \le \mathit{hi} \le n
\]

\[
\forall i \in [0, \mathit{lo}):\ a[i] < x
\quad\text{かつ}\quad
\forall j \in [\mathit{hi}, n):\ a[j] \ge x
\]

## 制約

- `a` は昇順にソート済みの `int` のリストです（空でもかまいません）。ソート済みであることの検査は不要です。
- `x` は `int` です。
- 標準ライブラリの `bisect` モジュールを使ってはいけません。
- 不変条件のうち量化子 \(\forall\) を含む部分は、`all()` と `range()` を組み合わせた式で `assert` してください。
- `assert` 文は最適化モード（`-O` オプション）では実行されません。返り値の計算に必要な処理を `assert` 文の中に書いてはいけません。

## 例

```python
>>> bisect_left([1, 3, 3, 5], 3)
1
>>> bisect_left([1, 3, 3, 5], 4)
3
>>> bisect_left([1, 3, 3, 5], 0)
0
>>> bisect_left([1, 3, 3, 5], 6)
4
>>> bisect_left([], 42)
0
>>> all(bisect_left(list(range(100)), x) == x for x in range(100))
True

```

## 発展

同じ流儀でループ不変条件を表明しながら `bisect_right(a, x)` を実装し、任意の入力で `bisect_left(a, x) <= bisect_right(a, x)` が成り立つことを確認してください。
また、不変条件の `assert` が計算量に与える影響（1周あたり \(O(n)\)）を見積もり、`-O` オプションの意義を説明してください。

## 参考

- 『Python Distilled』第3章「アサートと`__debug__`」
- [ループ不変条件 - Wikipedia](https://ja.wikipedia.org/wiki/ループ不変条件)
