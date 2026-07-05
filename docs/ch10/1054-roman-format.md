---
title: "1054: __format__ とローマ数字"
description: "整数を包むクラスに __format__ を実装し、f文字列から使える独自の書式ミニ言語でローマ数字表記を提供します。"
difficulty: 3
---

# 1054: \_\_format\_\_ とローマ数字

## 問題

組み込み関数 `format(value, format_spec)` は、内部的に `type(value).__format__(value, format_spec)` を呼び出します。
f文字列の `f"{value:spec}"` も同じ仕組みで動くため、`__format__` を実装したクラスは自分専用の書式ミニ言語を持てます。

題材としてローマ数字を選びます。
ローマ数字は記号の値を足し合わせる**加算的記数法**に、`IV`（4）や `CM`（900）のような減算則を加えたものです。
位取り記数法と違って桁の位置が値を決めず、ゼロの記号を持たず、標準的な減算則の下では 1 から 3999 までしか表せません。

クラス `Roman` を実装してください。

- `Roman(value)`：1 以上 3999 以下の `int` を包みます。
- `__format__(self, spec)` は書式指定子 `spec` を次のように解釈します。
    - `'r'` または空文字列：減算則を使った大文字のローマ数字表記
    - `'d'`：10進表記
    - それ以外：`ValueError` を送出

f文字列 `f"{Roman(2026):r}"` でそのまま使えることが要件です。

## 制約

- `value` が `int` でなければ `TypeError` を送出します。
- `value` が 1 以上 3999 以下でなければ `ValueError` を送出します。
- ローマ数字表記では減算則（`IV`, `IX`, `XL`, `XC`, `CD`, `CM`）を必ず使います。`IIII` のような加算だけの表記は使いません。
- 書式の解釈は `__format__` の実装だけで行い、`format` 組み込み関数や f文字列側に特別な細工はしません。

## 例

```python
>>> f"{Roman(2026):r}"
'MMXXVI'
>>> f"{Roman(1994):r}"
'MCMXCIV'
>>> format(Roman(4), 'r')
'IV'
>>> format(Roman(3999), 'r')
'MMMCMXCIX'
>>> f"{Roman(42):d}"
'42'
>>> f"{Roman(9)}"
'IX'
>>> Roman(0)
Traceback (most recent call last):
  ...
ValueError: value must be in the range 1 to 3999
>>> Roman(4000)
Traceback (most recent call last):
  ...
ValueError: value must be in the range 1 to 3999
>>> f"{Roman(10):x}"
Traceback (most recent call last):
  ...
ValueError: unknown format code 'x' for Roman

```

## 発展

書式指定子を組み込み型の書式ミニ言語に寄せて拡張してください。

- `f"{Roman(4):>10r}"` のように、変換型の前に幅と整列（`<`, `>`, `^`）を指定できるようにする。
- 時計の文字盤で使われる `IIII` 式の表記（減算則を使わない純粋な加算的表記）のための変換型 `'a'` を追加する。

整列部分の処理を自前で書かずに済ませる方法があるかも検討してください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
- [ローマ数字 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%AD%E3%83%BC%E3%83%9E%E6%95%B0%E5%AD%97)
