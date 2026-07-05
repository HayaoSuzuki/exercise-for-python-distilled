---
title: "0404: 遅延属性"
description: "__getattr__ で初回アクセス時にだけ計算してインスタンス辞書に埋める遅延属性を実装する問題です。"
difficulty: 3
---

# 0404: 遅延属性

## 問題

必要になるまで計算を先送りし、一度計算した値を再利用する評価戦略を **call-by-need**（必要呼び）と呼びます。
この戦略を、Python の属性プロトコルで実現してください。

整数のリストを保持するクラス `LazyStats` を実装します。
コンストラクタは非空の `list[int]` を受け取り、通常の属性として `data`（受け取ったリスト）と `computations`（統計量を計算した回数、初期値 0）を持ちます。

属性 `total`（総和）、`minimum`（最小値）、`maximum`（最大値）は遅延属性とします。

- インスタンス生成の時点では計算せず、インスタンス辞書にも存在しません。
- 初めてアクセスされたときに `__getattr__` の中で計算し、`computations` を 1 増やし、結果を同名の属性としてインスタンス辞書に格納します。
- 2 回目以降のアクセスでは再計算しません。

`__getattr__` は通常の属性検索で名前が見つからなかったときにだけ呼び出されます。
したがって、計算結果をインスタンス辞書に埋めれば、それ以降のアクセスで `__getattr__` は呼ばれなくなります。
「例」では、`vars()` によるインスタンス辞書の観察と `computations` の値で、計算が一度しか起きないことを確認します。

## 制約

- `data` は非空の `list[int]` を仮定してかまいません。
- 遅延属性の計算は、属性ごとに高々 1 回とします。
- `total` / `minimum` / `maximum` / `data` / `computations` 以外の属性へのアクセスは、Python の標準形式のメッセージ（例：`'LazyStats' object has no attribute 'average'`）で `AttributeError` を送出します。
- `__getattribute__` をオーバーライドしてはいけません。
- プロパティや `functools.cached_property` を使ってはいけません（`__getattr__` で実装します）。

## 例

```python
>>> s = LazyStats([3, 1, 4, 1, 5])
>>> s.computations
0
>>> "total" in vars(s)
False
>>> s.total
14
>>> s.computations
1
>>> "total" in vars(s)
True
>>> s.total
14
>>> s.computations
1
>>> s.minimum
1
>>> s.maximum
5
>>> s.computations
3
>>> s.average
Traceback (most recent call last):
  ...
AttributeError: 'LazyStats' object has no attribute 'average'

```

## 発展

- 遅延属性の仕組みをクラスから切り離し、`class LazyStats(LazyAttributes): _lazy = {"total": sum, ...}` のように、サンク（引数なしで呼べる計算の包み）の辞書を宣言するだけで任意のクラスに遅延属性を追加できる基底クラス `LazyAttributes` を設計してください。
- `data` を変更すると計算済みの値と矛盾します。計算済みの遅延属性を破棄して再計算させるメソッド `invalidate()` を追加してください。

## 参考

- 『Python Distilled』第4章「属性プロトコル」
- [遅延評価 - Wikipedia](https://ja.wikipedia.org/wiki/%E9%81%85%E5%BB%B6%E8%A9%95%E4%BE%A1)
