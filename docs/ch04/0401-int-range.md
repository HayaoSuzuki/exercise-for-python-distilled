---
title: "0401: 半開区間を表すコンテナ"
description: "整数の半開区間を、長さ、所属判定、反復に対応させます。"
difficulty: 2
---

# 0401: 半開区間を表すコンテナ

## 問題

整数の半開区間 `[start, stop)` を表すクラス `IntRange` を実装してください。
`IntRange(start, stop)` は、`start` 以上 `stop` 未満の整数を含むオブジェクトです。

## 制約

- インスタンスは属性 `start` と `stop` を持ちます。
- `repr(r)` は `IntRange(start, stop)` という形の文字列を返します。
- `len(r)` は区間に含まれる整数の個数を返します。
- `x in r` は、整数 `x` が区間に含まれるかを返します。
- `list(r)` は、区間に含まれる整数を昇順に返します。
- `stop < start` のときは空の区間として扱います。

## 例

```python
>>> r = IntRange(2, 5)
>>> repr(r)
'IntRange(2, 5)'
>>> len(r)
3
>>> 3 in r
True
>>> 5 in r
False
>>> list(r)
[2, 3, 4]
>>> list(IntRange(5, 2))
[]

```

## 発展

2つの `IntRange` が同じ整数列を表すときに等しいと判定する `__eq__` を追加してください。

## 参考

- 『Python Distilled』第4章「オブジェクトの表現と表示」
- 『Python Distilled』第4章「コンテナプロトコル」
- 『Python Distilled』第4章「イテレータプロトコル」
