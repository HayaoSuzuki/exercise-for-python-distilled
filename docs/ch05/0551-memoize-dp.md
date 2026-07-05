---
title: "0551: メモ化デコレータと動的計画法"
description: "functools.wraps を使ったメモ化デコレータを自作し、重複部分問題を持つ再帰計算を多項式時間で扱います。"
difficulty: 3
---

# 0551: メモ化デコレータと動的計画法

## 問題

カタラン数 \(C_n\) は次の漸化式で定義されます。

\[
C_0 = 1, \qquad C_n = \sum_{i=0}^{n-1} C_i \, C_{n-1-i} \quad (n \ge 1)
\]

この漸化式をそのまま再帰関数にすると、同じ引数に対する呼び出し（重複部分問題）が繰り返し発生し、呼び出し回数は \(n\) について指数的に増大します。
一度計算した結果を引数をキーとして記録し、2回目以降は記録を返すようにすれば、各引数についての計算は1回で済み、呼び出し回数は多項式オーダーになります。
この手法は**メモ化**と呼ばれ、動的計画法の実現手段の1つです。

関数の返り値をメモ化するデコレータ `memoize` を実装してください。

- `@memoize` を付けた関数は、同じ位置引数で2回目以降に呼び出されたとき、元の関数を実行せずに記録済みの結果を返します。
- `functools.wraps` を使い、`__name__` や `__doc__` などのメタデータを元の関数から引き継ぎます。

## 制約

- 対象関数は位置引数のみで呼び出されるものとし、引数はすべてハッシュ可能とします。
- キーワード引数で呼び出された場合の動作は問いません。
- `functools.cache` や `functools.lru_cache` など、標準ライブラリのメモ化機構は使用しません。

## 例

```python
>>> counter = {"calls": 0}
>>> @memoize
... def catalan(n):
...     """n 番目のカタラン数を返す。"""
...     counter["calls"] += 1
...     if n == 0:
...         return 1
...     return sum(catalan(i) * catalan(n - 1 - i) for i in range(n))
>>> catalan(10)
16796
>>> counter["calls"]  # catalan(0) から catalan(10) までの 11 回だけ実行される
11
>>> catalan(10)  # 2 回目は記録済みの結果を返す
16796
>>> counter["calls"]
11
>>> catalan.__name__
'catalan'
>>> catalan.__doc__
'n 番目のカタラン数を返す。'

```

## 発展

キャッシュの命中回数と登録件数を `catalan.cache_info()` のような形で取得できるように拡張してください。
また、`@memoize` を外した `catalan(20)` の呼び出し回数を数え、メモ化した場合と比較してください。

## 参考

- 『Python Distilled』第5章「デコレータ」
- 『Python Distilled』第5章「再帰」
- [動的計画法 - Wikipedia](https://ja.wikipedia.org/wiki/動的計画法)
- [カタラン数 - Wikipedia](https://ja.wikipedia.org/wiki/カタラン数)
