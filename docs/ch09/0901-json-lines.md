---
title: "0901: JSON Lines を読む"
description: "1行に1つの JSON 値があるテキストを読み取り、Python オブジェクトのリストにします。"
difficulty: 2
---

# 0901: JSON Lines を読む

## 問題

1行に1つの JSON 値がある文字列 `text` を読み取り、Python オブジェクトのリストを返す関数 `load_json_lines(text: str) -> list[object]` を実装してください。
空行は無視します。

## 制約

- `text` は文字列です。
- 空文字列、または空白文字だけの文字列に対しては空のリストを返します。
- 各非空行は `json.loads()` と同じ規則で読み取ります。
- JSON として不正な行がある場合、`json.loads()` が送出する例外をそのまま送出します。

## 例

```python
>>> load_json_lines("")
[]
>>> load_json_lines('{"name": "Ada"}\n[1, 2]\ntrue\n')
[{'name': 'Ada'}, [1, 2], True]
>>> load_json_lines('\n  1\n\n  2\n')
[1, 2]
>>> load_json_lines("{bad}")
Traceback (most recent call last):
    ...
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

```

## 発展

読み込んだ各行の行番号も一緒に返す版を書いてください。

## 参考

- 『Python Distilled』第9章「I/Oの抽象化層」
- 『Python Distilled』第9章「I/O標準ライブラリ」の「`json`」
