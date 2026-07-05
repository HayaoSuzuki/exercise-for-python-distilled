---
title: "0503: 共有しないデフォルト引数"
description: "None をデフォルト値にして、呼び出し間でリストを共有しない関数を作ります。"
difficulty: 2
---

# 0503: 共有しないデフォルト引数

## 問題

タグ文字列 `tag` と既存タグ列 `tags` を受け取り、`tag` を末尾に加えた新しいリストを返す関数 `add_tag(tag, tags=None)` を実装してください。
`tags` が省略された場合は、`tag` だけを含む新しいリストを返します。

## 制約

- 返り値はリストです。
- `tags` が省略された呼び出し同士で、同じリストを共有してはいけません。
- `tags` が渡された場合、返り値には `tags` の要素を同じ順序で含め、その末尾に `tag` を加えます。
- 渡された `tags` は変更してはいけません。

## 例

```python
>>> add_tag("python")
['python']
>>> first = add_tag("python")
>>> second = add_tag("distilled")
>>> first
['python']
>>> second
['distilled']
>>> existing = ["book"]
>>> add_tag("python", existing)
['book', 'python']
>>> existing
['book']

```

## 発展

`tags` に同じ文字列がすでに含まれている場合は追加しない版を書いてください。

## 参考

- 『Python Distilled』第5章「デフォルト引数」
- 『Python Distilled』第5章「返り値」
