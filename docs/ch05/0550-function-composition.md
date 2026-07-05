---
title: "0550: 関数合成のモノイド"
description: "1引数関数の合成 compose と反復合成 iterate を実装し、関数合成がモノイドをなすことを確認します。"
difficulty: 3
---

# 0550: 関数合成のモノイド

## 問題

1引数関数の全体は、関数合成 \(\circ\) を演算とする代数構造をなします。
合成は結合律 \((f \circ g) \circ h = f \circ (g \circ h)\) を満たし、恒等写像 \(\mathrm{id}(x) = x\) が単位元 \(f \circ \mathrm{id} = \mathrm{id} \circ f = f\) になるため、この構造は**モノイド**と呼ばれます。

次の2つの関数を実装してください。

- `compose(*funcs)`：1引数関数を任意個受け取り、その合成関数を返します。`compose(f, g, h)(x)` は \((f \circ g \circ h)(x) = f(g(h(x)))\)、つまり右端の関数から順に適用します。`compose()` は恒等写像を返します。
- `iterate(f, n)`：関数 `f` を \(n\) 回合成した関数 \(f^n = f \circ f \circ \cdots \circ f\) を返します。`iterate(f, 0)` は恒等写像を返します。

## 制約

- `compose` の各引数と `iterate` の第1引数は、1引数の callable とします。
- `iterate` の `n` は `int` とします。`n` が負の場合は `ValueError("n must be non-negative")` を送出します。
- 返り値はいずれも1引数の callable とします。

## 例

```python
>>> def inc(x):
...     return x + 1
>>> def double(x):
...     return x * 2
>>> def square(x):
...     return x * x
>>> compose(double, inc)(5)  # double(inc(5))
12
>>> compose(inc, double)(5)  # inc(double(5))
11
>>> compose(square, double, inc)(3)  # square(double(inc(3)))
64
>>> compose()(42)  # 単位元（恒等写像）
42
>>> compose(compose(square, double), inc)(3) == compose(square, compose(double, inc))(3)  # 結合律
True
>>> iterate(double, 10)(1)
1024
>>> iterate(double, 0)(99)
99
>>> iterate(double, -1)
Traceback (most recent call last):
    ...
ValueError: n must be non-negative

```

## 発展

`compose` を「右端の関数だけは任意個の位置引数を受け取れる」ように一般化してください。
例えば `compose(double, operator.add)(3, 4)` が `14` を返すようにします。

## 参考

- 『Python Distilled』第5章「高階関数」
- 『Python Distilled』第5章「lambda式」
- [モノイド - Wikipedia](https://ja.wikipedia.org/wiki/モノイド)
