---
title: "0101: 行ごとの点数集計"
description: "空白区切りの行を読み取り、名前ごとの点数を合計します。"
difficulty: 2
---

# 0101: 行ごとの点数集計

## 問題

文字列 `text` を行ごとに読み取り、名前ごとの点数を合計する関数 `total_scores(text: str) -> dict[str, int]` を実装してください。
各行は、名前と点数を空白で区切った形式です。

## 制約

- 空行は無視します。
- 名前は空白を含まない文字列です。
- 点数は10進整数です。
- 同じ名前が複数回現れたら点数を合計します。
- 名前と点数の2項目だけを持たない行に対しては `ValueError` を送出します。
- 点数を整数に変換できない行に対しては `ValueError` を送出します。

## 例

```python
>>> total_scores("")
{}
>>> total_scores("Ada 10\nGrace 7\nAda 3\n")
{'Ada': 13, 'Grace': 7}
>>> total_scores("Alan -2\nAlan 5\n")
{'Alan': 3}
>>> total_scores("Ada")
Traceback (most recent call last):
    ...
ValueError: line must contain a name and a score（行 1）
>>> total_scores("Ada x")
Traceback (most recent call last):
    ...
ValueError: score must be an integer（行 1）

```

## 発展

点数の合計だけでなく、名前ごとの件数と平均点も返す関数を書いてください。

## 参考

- 『Python Distilled』第1章「文字列」
- 『Python Distilled』第1章「辞書」
- 『Python Distilled』第1章「イテレーションとループ」
- 『Python Distilled』第1章「例外」
