---
title: "0201: タプルの左回転"
description: "スライスと剰余演算を使い、タプルの要素を左へ回転します。"
difficulty: 2
---

# 0201: タプルの左回転

## 問題

整数のタプル `values` を左へ `k` 個回転する関数 `rotate_left(values: tuple[int, ...], k: int) -> tuple[int, ...]` を実装してください。
左へ1個回転するとは、先頭の要素を末尾へ移すことです。

## 制約

- `values` は整数のタプルです。
- `k` は整数です。
- `values` が空のときは空のタプルを返します。
- `k` が `len(values)` 以上でも正しく回転します。
- 入力のタプルを変更してはいけません。

## 例

```python
>>> rotate_left((), 3)
()
>>> rotate_left((1, 2, 3, 4), 1)
(2, 3, 4, 1)
>>> rotate_left((1, 2, 3, 4), 6)
(3, 4, 1, 2)
>>> rotate_left((1, 2, 3, 4), 0)
(1, 2, 3, 4)

```

## 発展

右回転を行う `rotate_right()` も実装し、左回転との関係を確かめてください。

## 参考

- 『Python Distilled』第2章「標準的な演算子」
- 『Python Distilled』第2章「シーケンス」
- 『Python Distilled』第2章「式」
