---
title: "0702: 合成で作る履歴付きスタック"
description: "内部リストを持つクラスとして、push と pop の履歴を残すスタックを作ります。"
difficulty: 2
---

# 0702: 合成で作る履歴付きスタック

## 問題

文字列を格納するスタック `HistoryStack` を実装してください。
内部にリストを持ち、`push(item)` と `pop()` で要素を出し入れします。
実行した操作は、公開属性 `history` に記録します。

## 制約

- `HistoryStack()` は空のスタックを作ります。
- `push(item)` は `item` をスタックの末尾に追加し、`("push", item)` を `history` に追加します。
- `pop()` は最後に追加された文字列を返し、`("pop", item)` を `history` に追加します。
- 空のスタックに対して `pop()` を呼んだ場合は `IndexError` を送出します。
- `len(stack)` は現在の要素数を返します。
- `list(stack)` は、古い要素から新しい要素の順に現在の内容を返します。

## 例

```python
>>> stack = HistoryStack()
>>> len(stack)
0
>>> stack.push("a")
>>> stack.push("b")
>>> list(stack)
['a', 'b']
>>> stack.pop()
'b'
>>> stack.history
[('push', 'a'), ('push', 'b'), ('pop', 'b')]

```

## 発展

`history` を外部から直接変更されないようにする設計を考えてください。

## 参考

- 『Python Distilled』第7章「インスタンス」
- 『Python Distilled』第7章「インスタンスの属性」
- 『Python Distilled』第7章「継承よりも合成」
