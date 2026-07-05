---
title: "0403: 不変連結リスト"
description: "cons セルによるイミュータブルな連結リストを実装し、構造共有をオブジェクトの同一性で確認する問題です。"
difficulty: 4
---

# 0403: 不変連結リスト

## 問題

**cons セル**（先頭要素と残りのリストへの参照の組）を単位とする、イミュータブルな単方向連結リスト `ConsList` を実装してください。

関数型言語で標準的な永続データ構造です。
リストへの「追加」は既存のリストを書き換えるのではなく、既存のリスト全体を共有する新しいリストを返します。
この共有を**構造共有**と呼びます。

次のインタフェースを実装します。

- `ConsList()`：空リストを作ります。
- `xs.cons(item)`：先頭に `item` を積んだ新しいリストを返します。`xs` は変更されず、新しいリストの残り部分として共有されます。既存のセルをコピーしてはいけないので、この操作は \(O(1)\) です。
- `xs.head` / `xs.tail`：先頭要素と、先頭を除いた残りのリストを返します。
- `__iter__`：先頭から順に要素を生成します。
- `__len__`：要素数を返します。
- `__contains__`：`item in xs` をサポートします。
- `__getitem__`：`xs[i]` で先頭から `i` 番目（0 始まり）の要素を返します。

構造共有が実際に起きていることは、`is` 演算子による同一性の比較で確認できます。
「例」の `ys.tail is xs.tail` を参照してください。

## 制約

- インスタンスはイミュータブルとします。属性への代入と削除は、メッセージ `ConsList is immutable` の `AttributeError` を送出します。
- 空リストの `head` と `tail` は、それぞれメッセージ `empty ConsList has no head` / `empty ConsList has no tail` の `ValueError` を送出します。
- `__getitem__` のインデックスは `int` とします。`int` 以外は `TypeError`、範囲外（負の値を含む）はメッセージ `ConsList index out of range` の `IndexError` を送出します。スライスはサポートしません。
- `cons` は \(O(1)\) とします。要素のコピーや再構築をしてはいけません。

## 例

```python
>>> empty = ConsList()
>>> len(empty)
0
>>> xs = empty.cons(3).cons(2).cons(1)
>>> list(xs)
[1, 2, 3]
>>> len(xs)
3
>>> xs.head
1
>>> list(xs.tail)
[2, 3]
>>> ys = xs.tail.cons(10)
>>> list(ys)
[10, 2, 3]
>>> list(xs)
[1, 2, 3]
>>> ys.tail is xs.tail
True
>>> 2 in xs
True
>>> 5 in xs
False
>>> xs[0]
1
>>> xs[2]
3
>>> xs[3]
Traceback (most recent call last):
  ...
IndexError: ConsList index out of range
>>> xs.head = 99
Traceback (most recent call last):
  ...
AttributeError: ConsList is immutable
>>> empty.head
Traceback (most recent call last):
  ...
ValueError: empty ConsList has no head

```

`ys` は `xs` を壊さずに作られ、しかも `xs.tail` 以降のセルをそのまま共有しています。

## 発展

- イテラブルからリストを構築するクラスメソッド `ConsList.from_iterable(items)` を追加してください。
- `__reversed__` を実装し、`reversed(xs)` をサポートしてください。
- `__eq__` と `__hash__` を実装し、要素列が等しいリスト同士を等値にしてください。ハッシュ値を各セルにキャッシュすると、共有部分の再計算を避けられます。

## 参考

- 『Python Distilled』第4章「コンテナプロトコル」
- 『Python Distilled』第4章「イテレータプロトコル」
- 『Python Distilled』第4章「オブジェクトの同一性と型」
- [永続データ構造 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%B0%B8%E7%B6%9A%E3%83%87%E3%83%BC%E3%82%BF%E6%A7%8B%E9%80%A0)
