---
title: "0400: 座標を表す小さなプロトコル"
description: "2次元の点を、表示、比較、反復の各プロトコルに対応させます。"
difficulty: 2
---

# 0400: 座標を表す小さなプロトコル

## 問題

2次元の点を表すクラス `Point2D` を実装してください。
`Point2D(x, y)` で座標を作り、表示、等価比較、長さ、反復に対応させます。

## 制約

- インスタンスは属性 `x` と `y` を持ちます。
- `repr(point)` は `Point2D(x, y)` という形の文字列を返します。
- 2つの `Point2D` は、`x` と `y` がともに等しいときだけ等しいとみなします。
- `len(point)` は常に `2` を返します。
- `tuple(point)` は `(x, y)` を返します。
- タプル `(x, y)` との比較では `False` を返します。

## 例

```python
>>> p = Point2D(3, 4)
>>> p.x
3
>>> p.y
4
>>> repr(p)
'Point2D(3, 4)'
>>> Point2D(3, 4) == Point2D(3, 4)
True
>>> Point2D(3, 4) == (3, 4)
False
>>> len(p)
2
>>> tuple(p)
(3, 4)

```

## 発展

`abs(point)` で原点からの距離を返すように、数値プロトコルを1つ追加してください。

## 参考

- 『Python Distilled』第4章「オブジェクトの表現と表示」
- 『Python Distilled』第4章「比較プロトコル」
- 『Python Distilled』第4章「コンテナプロトコル」
- 『Python Distilled』第4章「イテレータプロトコル」
