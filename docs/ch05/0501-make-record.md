---
title: "0501: 引数を束ねるレコード関数"
description: "位置専用引数、可変長引数、キーワード専用引数、可変長キーワード引数を1つの関数で扱います。"
difficulty: 2
---

# 0501: 引数を束ねるレコード関数

## 問題

関数 `make_record(name, /, *tags, active=True, **attrs)` を実装してください。
この関数は、名前、タグ、状態、任意の属性を1つの辞書にまとめて返します。

## 制約

- 返り値はキー `"name"`、`"tags"`、`"active"` を必ず持ちます。
- `"name"` の値は `name` です。
- `"tags"` の値は、`tags` をタプルにした値です。
- `"active"` の値は `active` です。
- `attrs` の各項目は返り値の辞書に追加します。
- `attrs` に `"name"`、`"tags"` のいずれかが含まれる場合は `ValueError` を送出します。

## 例

```python
>>> make_record("Ada")
{'name': 'Ada', 'tags': (), 'active': True}
>>> make_record("Ada", "math", "python", active=False, score=10)
{'name': 'Ada', 'tags': ('math', 'python'), 'active': False, 'score': 10}
>>> make_record("Ada", name="override")
Traceback (most recent call last):
    ...
ValueError: reserved attribute: name

```

## 発展

返り値を辞書ではなく、属性アクセスできる小さなクラスにしてみてください。

## 参考

- 『Python Distilled』第5章「可変長引数」
- 『Python Distilled』第5章「キーワード引数」
- 『Python Distilled』第5章「可変長キーワード引数」
- 『Python Distilled』第5章「位置専用引数」
