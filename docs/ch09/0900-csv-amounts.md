---
title: "0900: CSV の金額集計"
description: "CSV 形式のテキストを読み取り、名前ごとの金額を合計します。"
difficulty: 2
---

# 0900: CSV の金額集計

## 問題

CSV 形式の文字列 `text` を読み取り、名前ごとの金額を合計する関数 `sum_csv_amounts(text: str) -> dict[str, int]` を実装してください。
入力の1行目はヘッダで、少なくとも `name` 列と `amount` 列を持ちます。

## 制約

- 空文字列、または空白文字だけの文字列に対しては空の辞書を返します。
- `name` 列の値を返り値のキーにします。
- `amount` 列の値は10進整数として読み取ります。
- 同じ名前が複数回現れたら金額を合計します。
- `name` 列または `amount` 列がない場合は `ValueError` を送出します。
- CSV の引用符やカンマを含むフィールドは、標準ライブラリの `csv` と同じ規則で扱います。

## 例

```python
>>> text = "name,amount\nspam,2\nspam,3\neggs,1\n"
>>> sum_csv_amounts(text)
{'spam': 5, 'eggs': 1}
>>> sum_csv_amounts("")
{}
>>> sum_csv_amounts("name,amount\n\"green, tea\",4\n")
{'green, tea': 4}
>>> sum_csv_amounts("name\nspam\n")
Traceback (most recent call last):
    ...
ValueError: CSV must contain name and amount columns

```

## 発展

実際のファイルオブジェクトを受け取る版を作り、`pathlib.Path.open()` で開いたファイルから同じ集計を行ってください。

## 参考

- 『Python Distilled』第9章「I/Oの抽象化層」
- 『Python Distilled』第9章「I/O標準ライブラリ」の「`csv`」
- 『Python Distilled』第9章「I/O標準ライブラリ」の「`io`」
