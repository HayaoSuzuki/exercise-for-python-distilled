---
title: "0603: オンライン分散のコルーチン"
description: "send() で値を受け取るたびに平均と分散を Welford 法で更新する拡張ジェネレータを実装します。"
difficulty: 4
---

# 0603: オンライン分散のコルーチン

## 問題

数値を1つずつ受け取り、受け取るたびに「これまでの個数、平均、分散」を報告する拡張ジェネレータ `stats()` を実装してください。

```python
def stats() -> Generator[tuple[int, float, float] | None, float]: ...
```

使い方は次のとおりです。
生成したジェネレータ `s` に対し、まず `s.send(None)` で最初の `yield` 式まで進めます。
以後、`s.send(x)` を呼ぶたびに値 \(x\) を取り込み、タプル `(n, mean, variance)` を返します。
ここで \(n\) は受け取った値の個数、`mean` は平均 \(\bar{x}_n\)、`variance` は母分散

\[
\sigma_n^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{x}_n)^2
\]

です。

更新には **Welford 法**を使います。
\(\bar{x}_0 = 0\)、\(M_0 = 0\) とし、\(n\) 番目の値 \(x_n\) を受け取ったとき

\[
\bar{x}_n = \bar{x}_{n-1} + \frac{x_n - \bar{x}_{n-1}}{n},
\qquad
M_n = M_{n-1} + (x_n - \bar{x}_{n-1})(x_n - \bar{x}_n)
\]

と更新すると、\(\sigma_n^2 = M_n / n\) が得られます。

## 制約

- 受け取った値をリストなどの列として保持してはいけません。内部状態は個数、平均、\(M_n\) の3変数で、メモリ使用量は \(O(1)\) とします。
- 分散を \(\frac{1}{n}\sum x_i^2 - \bar{x}_n^2\) の形（二乗和の差）で求めてはいけません。この公式は \(|\bar{x}_n|\) が標準偏差に比べて大きいとき桁落ちし、浮動小数点演算では分散が負になることさえあります。
- 送られる値は `float` とします。\(n = 1\) のとき分散は `0.0` です。

## 例

```python
>>> s = stats()
>>> s.send(None)  # 最初の yield 式まで進める
>>> s.send(0.0)
(1, 0.0, 0.0)
>>> s.send(3.0)
(2, 1.5, 2.25)
>>> s.send(6.0)
(3, 3.0, 6.0)

```

`statistics.pvariance()` は内部で正確な演算を行うため、結果の検算に使えます。

```python
>>> import statistics
>>> data = [0.5 * k for k in range(1, 101)]
>>> s = stats()
>>> s.send(None)
>>> for x in data:
...     n, mean, var = s.send(x)
...
>>> (n, round(mean, 10))
(100, 25.25)
>>> round(var, 10) == round(statistics.pvariance(data), 10)
True

```

## 発展

- 制約で禁止した二乗和方式をあえて実装し、\(x_i = 10^9 + i\)（\(i = 1, \dots, 1000\)）のようにオフセットの大きいデータで、Welford 法および `statistics.pvariance()` の結果と比較してください。
- 不偏分散（\(n - 1\) で割る）も同時に返すよう拡張してください。さらに、三次と四次の中心モーメント（歪度、尖度）のオンライン更新式を調べて実装してください。

## 参考

- 『Python Distilled』第6章「拡張ジェネレータとyield式」
- 『Python Distilled』第6章「拡張ジェネレータの応用」
- [Algorithms for calculating variance - Wikipedia](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance)
