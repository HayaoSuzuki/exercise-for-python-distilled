---
title: "0302: 例外の連鎖を保つ再帰下降パーサ"
description: "四則演算と括弧からなる式を評価する再帰下降パーサを実装し、内部の例外を ParseError に連鎖させます。"
difficulty: 4
---

# 0302: 例外の連鎖を保つ再帰下降パーサ

## 問題

次の文法（EBNF）で定義される算術式を、再帰下降構文解析で評価します。
文法の各非終端記号を1つの関数に対応させると、文法の構造をそのままコードに写し取れます。

```
expr   ::= term (("+" | "-") term)*
term   ::= factor (("*" | "/") factor)*
factor ::= integer | "(" expr ")"
```

`integer` は 0 以上の整数リテラルです。
トークンの間には空白を置けます。

次の2つを実装してください。

- `Exception` を継承したユーザ定義例外 `ParseError`。
- 関数 `evaluate(src: str) -> int | float`。式文字列 `src` を上の文法に従って解析し、値を計算して返します。

エラー処理は次の仕様に従ってください。

- `src` が文法に合わない場合（不正な文字、括弧の不一致、入力の途中終了、余分な入力など）は `ParseError` を送出します。
- 計算中に発生した `ZeroDivisionError` は、`raise ... from` で `ParseError` に包んで送出します。捕捉した `ParseError` の `__cause__` 属性から、元の `ZeroDivisionError` をたどれる必要があります。

## 制約

- 入力は `str` 型です。
- 演算子の意味は Python と同じです。`+`、`-`、`*` は整数同士なら `int` を返し、`/` は真の除算（結果は `float`）です。
- 2項演算子はすべて左結合です。
- 単項マイナス（`-3` など）は扱いません。
- `eval()` や `ast` モジュールなど、Python の式評価機構を使ってはいけません。
- 0 除算を素通しにせず、必ず `ParseError` に包んで送出してください。

## 例

```python
>>> evaluate("1 + 2 * 3")
7
>>> evaluate("(1 + 2) * 3")
9
>>> evaluate("7 / 2")
3.5
>>> evaluate("2 * (3 + 4) - 5")
9
>>> try:
...     evaluate("(1 + 2")
... except ParseError:
...     print("syntax error")
syntax error
>>> try:
...     evaluate("10 / (3 - 3)")
... except ParseError as e:
...     print(type(e.__cause__).__name__)
ZeroDivisionError

```

## 発展

右結合のべき乗演算子 `**` と単項マイナスを文法に追加してください。
また、構文エラーの `ParseError` に、エラーが起きた位置（`src` 中のインデックス）を属性として持たせてください。

## 参考

- 『Python Distilled』第3章「ユーザ定義例外」
- 『Python Distilled』第3章「例外の連鎖」
- [再帰下降構文解析 - Wikipedia](https://ja.wikipedia.org/wiki/再帰下降構文解析)
