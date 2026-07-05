---
title: "0755: __slots__ で作る Union-Find"
description: "__slots__ を持つクラスとして素集合データ構造（Union-Find）を実装します。"
difficulty: 3
---

# 0755: \_\_slots\_\_ で作る Union-Find

## 問題

**素集合データ構造**（Union-Find）は、互いに素な集合の族を管理し、2 要素が同じ集合に属するかの判定と 2 つの集合の併合を高速に行います。
経路圧縮とランクによる併合を併用すると、1 操作あたりのならし計算量は \(O(\alpha(n))\)（\(\alpha\) はアッカーマン関数の逆関数で、実用上は定数）になります。
インスタンス属性が固定されたデータ構造なので、`__slots__` を指定してインスタンス辞書を持たない軽量なクラスとして実装します。
これにより、属性名のタイプミスによる代入も実行時エラーとして検出されます。

クラス `DisjointSet` を実装してください。

- `DisjointSet(n)`:要素 `0` から `n - 1` を、それぞれ単独の集合として初期化する。
- `find(x)`:`x` の属する集合の代表元を返す。
- `union(x, y)`:`x` の集合と `y` の集合を併合する。併合したら `True` を、はじめから同じ集合なら `False` を返す。
- `connected(x, y)`:`x` と `y` が同じ集合に属するかを返す。
- `count`:現在の集合の個数（読み出し専用プロパティ）。
- クラスに `__slots__` を定義し、インスタンスが `__dict__` を持たないようにする。

## 制約

- `n` は非負整数とします。負の場合は `ValueError` を送出します。
- 要素は `0 <= x < n` の整数とします。範囲外の場合は `IndexError`（メッセージは `element <x> is out of range`）を送出します。
- `find` には経路圧縮を、`union` にはランク（またはサイズ）による併合を実装します。

## 例

```python
>>> ds = DisjointSet(5)
>>> ds.count
5
>>> ds.union(0, 1)
True
>>> ds.union(1, 2)
True
>>> ds.union(0, 2)   # すでに同じ集合
False
>>> ds.connected(0, 2)
True
>>> ds.connected(0, 3)
False
>>> ds.count
3
>>> ds.find(0) == ds.find(2)
True
>>> ds.find(5)
Traceback (most recent call last):
    ...
IndexError: element 5 is out of range

```

`__slots__` を定義したので、インスタンスは `__dict__` を持たず、宣言していない属性への代入は失敗します。

```python
>>> hasattr(ds, "__dict__")
False
>>> ds.n_elements = 5
Traceback (most recent call last):
    ...
AttributeError: 'DisjointSet' object has no attribute 'n_elements' and no __dict__ for setting new attributes

```

## 発展

1. `__slots__` を外した実装と、`tracemalloc` を使ってメモリ使用量を比較してください。
2. 空でない `__slots__` を持つ 2 つのクラスを多重継承するとどうなるかを確認してください。
3. `count` を使って、`n` 頂点 `m` 辺の無向グラフの連結成分数を数える関数を書いてください。

## 参考

- 『Python Distilled』第7章「`__slots__`によるメモリ使用量の削減」
- 『Python Distilled』第7章「内部オブジェクトの表現と属性束縛」
- [素集合データ構造 - Wikipedia](https://ja.wikipedia.org/wiki/素集合データ構造)
