---
title: "0401: 剰余環 Z/nZ"
description: "剰余環の元を表すクラスを数値プロトコルで実装し、__eq__ と __hash__ の整合性を保つ問題です。"
difficulty: 3
---

# 0401: 剰余環 Z/nZ

## 問題

整数 \(n \ge 2\) に対し、剰余環 \(\mathbb{Z}/n\mathbb{Z}\) の元を表すクラス `Mod` を実装してください。

`Mod(value, modulus)` は、整数 `value` の法 `modulus` に関する剰余類を表します。
内部の代表元は \(0 \le v < n\) の範囲に正規化します。

次の特殊メソッドを実装します。

- `__add__` / `__sub__` / `__mul__`：同じ法を持つ `Mod` 同士の和・差・積を計算し、`Mod` を返します。
- `__pow__`：`int` の指数によるべき乗を計算します。
- `__eq__`：法が等しく、かつ剰余が等しいときに限り `True` を返します。
- `__hash__`：`__eq__` と整合させます。すなわち、等しい 2 つのインスタンスは同じハッシュ値を持ち、`Mod` を集合の要素や辞書のキーとして使えるようにします。
- `__repr__`：`eval()` で同じ値のオブジェクトを再作成できる文字列 `Mod(2, 7)` の形式を返します。

なお、\(\mathbb{Z}/n\mathbb{Z}\) は \(n\) が合成数のとき零因子（どちらも \(0\) でないのに積が \(0\) になる元の組）を持ちます。
「例」の最後で、この現象を確認します。

## 制約

- `value` と `modulus` は `int` とします。いずれかが `int` でなければ `TypeError` を送出します。
- `modulus < 2` の場合は `ValueError` を送出します。
- 法の異なる `Mod` 同士の `+` / `-` / `*` は、メッセージ `cannot operate on Mod objects with different moduli: <m1> and <m2>` の `TypeError` を送出します。
- `Mod` と `int` を混ぜた算術演算はサポートしません。オペランドが `Mod` 以外の場合は `NotImplemented` を返し、Python に `TypeError` を送出させます。
- `__pow__` の指数が `int` でない場合も `NotImplemented` を返します。指数は 0 以上を仮定してかまいません（負の指数は「発展」で扱います）。
- 法の異なる `Mod` 同士の `==` は、例外ではなく `False` になるようにします。

## 例

```python
>>> a = Mod(3, 7)
>>> b = Mod(5, 7)
>>> a + b
Mod(1, 7)
>>> a - b
Mod(5, 7)
>>> a * b
Mod(1, 7)
>>> a ** 6
Mod(1, 7)
>>> Mod(10, 7) == Mod(3, 7)
True
>>> Mod(3, 5) == Mod(3, 7)
False
>>> hash(Mod(10, 7)) == hash(Mod(3, 7))
True
>>> len({Mod(3, 7), Mod(10, 7), Mod(4, 7)})
2
>>> eval(repr(Mod(11, 7))) == Mod(4, 7)
True
>>> Mod(1, 5) + Mod(1, 7)
Traceback (most recent call last):
  ...
TypeError: cannot operate on Mod objects with different moduli: 5 and 7
>>> Mod(2, 6) * Mod(3, 6)
Mod(0, 6)

```

## 発展

- 負の指数をサポートしてください。`Mod(3, 7) ** -1` は法逆元 `Mod(5, 7)` を返し、逆元が存在しない場合（代表元と法が互いに素でない場合）は `ValueError` を送出します。
- 単元（乗法逆元を持つ元）だけを集めると群になります。与えられた法 \(n\) に対して単元群 \((\mathbb{Z}/n\mathbb{Z})^\times\) の元をすべて列挙するクラスメソッドを追加し、その個数がオイラーの \(\varphi\) 関数と一致することを確認してください。

## 参考

- 『Python Distilled』第4章「数値プロトコル」
- 『Python Distilled』第4章「比較プロトコル」
- 『Python Distilled』第4章「オブジェクトプロトコル」
- [剰余類環 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%89%B0%E4%BD%99%E9%A1%9E%E7%92%B0)
