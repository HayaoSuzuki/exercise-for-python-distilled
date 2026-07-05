---
title: "0703: メタクラスによるハッシュコンシング"
description: "メタクラスの __call__ をメモ化し、同じ引数からは同一のインスタンスを返すハッシュコンシングを実装します。"
difficulty: 4
---

# 0703: メタクラスによるハッシュコンシング

## 問題

同じ内容の不変オブジェクトを一度だけ生成して共有する技法を**ハッシュコンシング**（hash consing）と呼びます。
生成済みのオブジェクトを、コンストラクタ引数をキーとする表で管理し、2 回目以降の生成要求には既存のオブジェクトを返します。
等価なオブジェクトが常に同一（`is` が `True`）になるため、等価性の判定を同一性の判定に帰着でき、重複するインスタンスを減らせます。
デザインパターンで言えばフライウェイトにあたります。

インスタンスの生成（クラスの呼び出し）はメタクラスの `__call__()` が制御しています。
そこで、この動作をクラスごとに書き換えるのではなく、メタクラスとして一括して差し替えます。

メタクラス `InternMeta` を実装してください。

- `type` を継承する。
- `__call__()` をオーバーライドし、位置引数のタプルをキーとしてインスタンスをメモ化する。
- 同じ引数でクラスが呼ばれたら、`__new__()` と `__init__()` を実行せずに、以前と同一のインスタンスを返す。
- メモ化の表はクラスごとに独立させる。

## 制約

- コンストラクタの引数は位置引数のみとします。キーワード引数は扱わなくてかまいません。
- 引数はハッシュ可能とします。ハッシュ不能な引数に対しては `TypeError` が送出されます（組み込みの送出に任せてかまいません）。
- インスタンスは生成後に変更されない（不変とみなす）前提でかまいません。

## 例

```python
>>> class Symbol(metaclass=InternMeta):
...     def __init__(self, name):
...         self.name = name
...
>>> Symbol("x") is Symbol("x")
True
>>> Symbol("x") is Symbol("y")
False
>>> class Counter(metaclass=InternMeta):
...     created = 0
...     def __init__(self, key):
...         type(self).created += 1
...
>>> a = Counter("k")
>>> b = Counter("k")
>>> a is b
True
>>> Counter.created  # __init__ は一度しか実行されない
1
>>> class Pair(metaclass=InternMeta):
...     def __init__(self, head, tail):
...         self.head = head
...         self.tail = tail
...
>>> Pair(1, Pair(2, None)) is Pair(1, Pair(2, None))
True
>>> Symbol(["x", "y"])
Traceback (most recent call last):
    ...
TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list')

```

## 発展

この実装では、メモ化の表がインスタンスを強参照し続けるため、どこからも使われなくなったインスタンスも解放されません。
表を `weakref.WeakValueDictionary` に置き換えて、参照されなくなったインスタンスが表から自動的に消えるようにしてください（問題 0704 も参照）。

## 参考

- 『Python Distilled』第7章「メタクラス」
- 『Python Distilled』第7章「オブジェクトのライフサイクルとメモリ管理」
- [Hash consing - Wikipedia](https://en.wikipedia.org/wiki/Hash_consing)
- [Flyweight パターン - Wikipedia](https://ja.wikipedia.org/wiki/Flyweight_パターン)
