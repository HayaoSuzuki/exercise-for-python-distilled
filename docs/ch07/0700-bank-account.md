---
title: "0700: 残高を管理するクラス"
description: "インスタンス属性、プロパティ、クラスメソッドを使って小さなクラスを作ります。"
difficulty: 2
---

# 0700: 残高を管理するクラス

## 問題

口座を表すクラス `BankAccount` を実装してください。
口座は所有者名 `owner` と残高を持ち、入金と出金を行えます。

## 制約

- `BankAccount(owner, balance=0)` で口座を作ります。
- `owner` は公開属性として読み書きできます。
- `balance` は読み取り専用のプロパティです。
- 初期残高が負のときは `ValueError` を送出します。
- `deposit(amount)` は正の整数を受け取り、残高を増やして新しい残高を返します。
- `withdraw(amount)` は正の整数を受け取り、残高を減らして新しい残高を返します。
- 入金額または出金額が正でないときは `ValueError` を送出します。
- 出金額が残高を超えるときは `ValueError` を送出します。
- `BankAccount.from_text("Ada:120")` は、所有者名と残高を `:` で区切った文字列から口座を作ります。

## 例

```python
>>> account = BankAccount("Ada", 100)
>>> account.owner
'Ada'
>>> account.balance
100
>>> account.deposit(40)
140
>>> account.withdraw(15)
125
>>> BankAccount.from_text("Grace:200").balance
200
>>> BankAccount("Ada", -1)
Traceback (most recent call last):
    ...
ValueError: balance must be non-negative

```

## 発展

所有者名を変更できない読み取り専用プロパティにし、表示用の `__repr__` も追加してください。

## 参考

- 『Python Distilled』第7章「class文」
- 『Python Distilled』第7章「インスタンス」
- 『Python Distilled』第7章「インスタンスの属性」
- 『Python Distilled』第7章「クラス変数とクラスメソッド」
- 『Python Distilled』第7章「プロパティ」
