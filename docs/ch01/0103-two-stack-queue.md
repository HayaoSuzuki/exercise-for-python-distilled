---
title: "0103: スタック2つで作るキュー"
description: "append と pop しかできないスタック2本から、償却 O(1) のキューを組み立てます。"
difficulty: 3
---

# 0103: スタック2つで作るキュー

## 問題

Python の `list` は、末尾への `append()` と末尾からの `pop()` が \(O(1)\) で動くスタックです。
一方、先頭からの取り出し（`pop(0)`）は要素の詰め直しが起きるため \(O(n)\) かかります。
スタックを2本組み合わせると、この詰め直しなしに先入れ先出し（FIFO）のキューを作れることが知られています。

クラス `Queue` を実装してください。

- `enqueue(item)`：`item` をキューの末尾に追加します。
- `dequeue()`：キューの先頭の要素を取り除いて返します。
- `len(q)`：キューに残っている要素数を返します。

任意の操作列に対して、`enqueue()` と `dequeue()` は償却 \(O(1)\) でなければなりません。
すなわち、\(m\) 回の操作全体にかかる時間が \(O(m)\) に収まる必要があります。

## 制約

- 要素を保持するコンテナは `list` 2本だけとします。
- `list` の要素の追加と削除は `append()` と引数なしの `pop()` のみ使えます。`pop(0)` や `insert()`、スライス、`reversed()` による並べ替えは使いません。
- `collections.deque` などの既製のキューは使いません。
- 空のキューに対する `dequeue()` は `IndexError` を送出します。
- `len()` は \(O(1)\) とします。

## 例

```python
>>> q = Queue()
>>> q.enqueue("a")
>>> q.enqueue("b")
>>> q.dequeue()
'a'
>>> q.enqueue("c")
>>> len(q)
2
>>> q.dequeue()
'b'
>>> q.dequeue()
'c'
>>> q.dequeue()
Traceback (most recent call last):
  ...
IndexError: dequeue from empty queue

```

## 発展

実装が償却 \(O(1)\) であることを、次のポテンシャル関数で示してください。
キューの状態に対して \(\Phi = 2 \times (\text{入力側スタックの要素数})\) とおくと、各操作の償却コスト（実コストと \(\Phi\) の増分の和）が定数で抑えられることを確かめます。

さらに、そのとき保持している要素の最小値を \(O(1)\) で返す `min()` メソッドを、償却計算量を変えずに追加してください。

## 参考

- 『Python Distilled』第1章「リスト」
- 『Python Distilled』第1章「オブジェクトとクラス」
- 『Python Distilled』第1章「例外」
- [Amortized analysis - Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)
