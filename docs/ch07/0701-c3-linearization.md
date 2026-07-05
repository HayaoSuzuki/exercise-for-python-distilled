---
title: "0701: C3線型化の実装"
description: "クラス名の継承グラフからメソッド解決順序を計算する C3 線型化アルゴリズムを実装します。"
difficulty: 5
---

# 0701: C3線型化の実装

## 問題

Python はクラスの継承関係から、属性検索の順序である**メソッド解決順序**（Method Resolution Order: MRO）を C3 線型化アルゴリズムで計算します。
このアルゴリズムを、実際のクラスの代わりにクラス名だけで表した継承グラフに対して実装します。
継承グラフは、クラス名を基底クラス名のリストに対応させる辞書で表し、基底クラスを持たないクラスには空リストを対応させます。

関数 `linearize(name: str, graph: dict[str, list[str]]) -> list[str]` を実装してください。
返り値はクラス `name` の線型化で、クラス名を検索順に並べたリストです。

C3 線型化は次の規則で定義されます。
クラス \(C\) の基底クラスが順に \(B_1, \dots, B_n\) のとき

\[
L(C) = C \cdot \operatorname{merge}(L(B_1), \dots, L(B_n), [B_1, \dots, B_n])
\]

であり、基底クラスを持たないクラスでは \(L(C) = [C]\) です。
\(\operatorname{merge}\) は、与えられた列を次の手続きで 1 つの列に統合します。

1. 列を前から順に調べ、その先頭要素が「どの列でも先頭以外の位置に現れない」ような最初の列を探す。
2. 見つかった先頭要素を結果に追加し、すべての列からその要素を取り除く（空になった列は捨てる）。
3. すべての列が空になるまで 1 と 2 を繰り返す。
4. 手順 1 で条件を満たす先頭要素が 1 つも見つからなければ、線型化は存在しない。

## 制約

- `graph` に出現するクラス名は、すべて `graph` のキーとして存在します。
- 継承グラフは有向非巡回グラフです。循環を含む入力は扱いません。
- 線型化が存在しない場合は `TypeError` を送出します。メッセージは `Cannot create a consistent method resolution order (MRO) for <クラス名>` とします。
- `type()` の動的呼び出しなどで実際にクラスを生成し、Python 本体に MRO を計算させてはいけません。

## 例

```python
>>> graph = {
...     "object": [],
...     "X": ["object"],
...     "Y": ["object"],
...     "A": ["X", "Y"],
...     "B": ["Y", "X"],
... }
>>> linearize("X", graph)
['X', 'object']
>>> linearize("A", graph)
['A', 'X', 'Y', 'object']
>>> linearize("B", graph)
['B', 'Y', 'X', 'object']
>>> graph["Z"] = ["A", "B"]
>>> linearize("Z", graph)
Traceback (most recent call last):
    ...
TypeError: Cannot create a consistent method resolution order (MRO) for Z

```

実際のクラスが持つ `__mro__` と一致することも確認できます。

```python
>>> class X: pass
>>> class Y: pass
>>> class A(X, Y): pass
>>> [c.__name__ for c in A.__mro__]
['A', 'X', 'Y', 'object']
>>> [c.__name__ for c in A.__mro__] == linearize("A", graph)
True

```

## 発展

C3 線型化は、**単調性**（あるクラスの線型化における 2 クラスの順序が、その派生クラスの線型化でも保存される）と**局所優先順序の保存**（継承リストに書いた基底クラスの順序が線型化でも保存される）を満たします。
ランダムに生成した非巡回の継承グラフに対して、`linearize` の結果がこの 2 性質を満たすことを検査するテストを書いてください。

## 参考

- 『Python Distilled』第7章「多重継承、インタフェース、ミックスイン」
- [The Python 2.3 Method Resolution Order](https://docs.python.org/3/howto/mro.html)
- K. Barrett, et al., "A Monotonic Superclass Linearization for Dylan", OOPSLA '96
- [C3 linearization - Wikipedia](https://en.wikipedia.org/wiki/C3_linearization)
