---
title: "0500: 状態を持つ累算関数"
description: "外側の関数で作った状態を、内側の関数から更新します。"
difficulty: 2
---

# 0500: 状態を持つ累算関数

## 問題

整数を累算する関数を作る `make_accumulator(initial: int = 0)` を実装してください。
`make_accumulator()` は、整数 `value` を受け取る関数を返します。
返された関数は、呼び出されるたびに内部の合計へ `value` を足し、新しい合計を返します。

## 制約

- `initial` は初期値です。
- 返された関数は `value: int` を1つ受け取ります。
- `make_accumulator()` を複数回呼び出したとき、それぞれの累算状態は独立していなければなりません。
- グローバル変数で合計を共有してはいけません。

## 例

```python
>>> acc = make_accumulator(10)
>>> acc(5)
15
>>> acc(-3)
12
>>> other = make_accumulator()
>>> other(7)
7
>>> acc(1)
13

```

## 発展

現在の合計をリセットする操作も持つ小さなオブジェクトとして実装し直してください。

## 参考

- 『Python Distilled』第5章「関数定義」
- 『Python Distilled』第5章「デフォルト引数」
- 『Python Distilled』第5章「副作用のある関数」
- 『Python Distilled』第5章「スコープルール」
- 『Python Distilled』第5章「高階関数」
