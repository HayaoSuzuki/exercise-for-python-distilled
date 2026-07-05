---
title: "0300: 最初の重複値"
description: "列を左から調べ、2回目に現れた値を返します。"
difficulty: 2
---

# 0300: 最初の重複値

## 問題

整数列 `values` を左から順に調べ、すでに現れたことのある値に初めて出会ったら、その値を返す関数 `first_duplicate(values)` を実装してください。
重複がなければ `None` を返します。

## 制約

- `values` は整数のイテラブルです。
- 返す値は、2回目の出現位置が最も左にある値です。
- 入力の要素順を変更してはいけません。
- 重複がない場合に例外を送出してはいけません。

## 例

```python
>>> first_duplicate([])
>>> first_duplicate([1, 2, 3])
>>> first_duplicate([3, 1, 3, 1])
3
>>> first_duplicate([2, 1, 1, 2])
1
>>> first_duplicate([-1, 0, -1])
-1

```

## 発展

重複した値そのものではなく、最初の重複が見つかった位置を返す関数を書いてください。

## 参考

- 『Python Distilled』第3章「条件分岐」
- 『Python Distilled』第3章「ループとイテレーション」
