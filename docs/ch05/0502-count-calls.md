---
title: "0502: 呼び出し回数を数えるデコレータ"
description: "関数を包み、呼び出された回数を属性として持つデコレータを作ります。"
difficulty: 2
---

# 0502: 呼び出し回数を数えるデコレータ

## 問題

関数を受け取り、呼び出し回数を記録するデコレータ `count_calls(func)` を実装してください。
`count_calls` が返す callable は、属性 `calls` にこれまで呼び出された回数を保持します。

## 制約

- `calls` の初期値は `0` です。
- ラップした callable が呼ばれるたびに、`calls` を1増やします。
- 引数と返り値は、元の関数にそのまま渡します。
- 元の関数名は `__name__` から参照できるようにします。

## 例

```python
>>> @count_calls
... def add(x, y):
...     return x + y
...
>>> add.calls
0
>>> add(2, 3)
5
>>> add.calls
1
>>> add.__name__
'add'

```

## 発展

呼び出し回数だけでなく、最後に渡された引数も記録する版を書いてください。

## 参考

- 『Python Distilled』第5章「スコープルール」
- 『Python Distilled』第5章「高階関数」
- 『Python Distilled』第5章「デコレータ」
