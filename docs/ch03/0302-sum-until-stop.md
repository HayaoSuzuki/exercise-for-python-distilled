---
title: "0302: STOP までの合計"
description: "行を順に処理し、空行を読み飛ばしながら STOP が現れるまで整数を合計します。"
difficulty: 2
---

# 0302: STOP までの合計

## 問題

文字列のイテラブル `lines` を先頭から読み、`"STOP"` が現れるまで整数として合計する関数 `sum_until_stop(lines)` を実装してください。
各行の前後の空白は無視します。

## 制約

- 空白だけの行は合計に含めず、次の行へ進みます。
- 前後の空白を除いた値が `"STOP"` の行で処理を終了します。
- `"STOP"` より後ろの行は読みません。
- 空行でも `"STOP"` でもない行は10進整数として扱います。
- 整数として読めない行があれば `ValueError` を送出します。
- `ValueError` のメッセージは `invalid integer: 値` とします。

## 例

```python
>>> sum_until_stop(["10", " 5 ", "", "STOP", "100"])
15
>>> sum_until_stop(["-2", "3"])
1
>>> sum_until_stop(["1", "x"])
Traceback (most recent call last):
    ...
ValueError: invalid integer: x

```

## 発展

`"STOP"` 以外の終了語を引数で指定できる版を書いてください。

## 参考

- 『Python Distilled』第3章「条件分岐」
- 『Python Distilled』第3章「ループとイテレーション」
- 『Python Distilled』第3章「例外」
