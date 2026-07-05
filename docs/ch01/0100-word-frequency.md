---
title: "0100: 単語頻度表"
description: "空白で区切った単語を小文字化し、辞書で出現回数を数えます。"
difficulty: 2
---

# 0100: 単語頻度表

## 問題

文字列 `text` から単語頻度表を作る関数 `word_frequencies(text: str) -> dict[str, int]` を実装してください。
単語は `str.split()` と同じ規則で空白により分けます。
大文字と小文字は区別せず、すべて小文字にして数えます。

## 制約

- `text` は `str` です。
- 空文字列、または空白文字だけの文字列に対しては空の辞書を返します。
- 句読点や記号は取り除かず、単語の一部として扱います。
- 返り値の辞書は、単語が最初に現れた順序を保ちます。

## 例

```python
>>> word_frequencies("")
{}
>>> word_frequencies("Spam spam eggs")
{'spam': 2, 'eggs': 1}
>>> word_frequencies("  one\tone\nTWO  ")
{'one': 2, 'two': 1}
>>> word_frequencies("hello, hello")
{'hello,': 1, 'hello': 1}

```

## 発展

句読点を取り除く処理を加えた関数を別に作り、同じ入力で頻度表がどう変わるかを確かめてください。

## 参考

- 『Python Distilled』第1章「文字列」
- 『Python Distilled』第1章「辞書」
- 『Python Distilled』第1章「イテレーションとループ」
- 『Python Distilled』第1章「関数」
