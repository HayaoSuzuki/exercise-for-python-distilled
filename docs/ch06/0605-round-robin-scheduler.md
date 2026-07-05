---
title: "0605: ラウンドロビン・スケジューラ"
description: "ジェネレータをタスクとして登録し deque でラウンドロビン実行する協調的スケジューラを実装します。"
difficulty: 5
---

# 0605: ラウンドロビン・スケジューラ

## 問題

ジェネレータを協調的タスクとして実行するラウンドロビン・スケジューラ `Scheduler` を実装してください。
asyncio のイベントループの原型にあたる仕組みで、タスクは `yield` で自発的に制御を手放し、スケジューラが次のタスクへ実行を切り替えます。

```python
class Scheduler:
    def add(self, task: Iterator[object]) -> None: ...
    def run(self) -> None: ...
```

仕様は次のとおりです。

- `add(task)` はジェネレータをタスクとして実行キューの末尾に登録します。
- `run()` は、キューの先頭からタスクを取り出して次の `yield` まで実行し、まだ終了していなければ末尾に戻す、という周回をキューが空になるまで繰り返します。
- タスクの終了は `StopIteration` で検出し、終了したタスクはキューに戻しません。
- 実行中のタスクは `add()` で新しいタスクを登録できます。登録されたタスクはキューの末尾に加わり、以後の周回で実行されます。

## 制約

- 実行キューには `collections.deque` を使います。
- スレッド、asyncio、その他の並行処理ライブラリを使ってはいけません。
- タスクが `yield` で渡す値は無視して構いません（発展で扱います）。
- タスク内で送出された `StopIteration` 以外の例外は、`run()` の中で握りつぶさずそのまま伝播させます。

## 例

タスクは登録順に1周ずつ実行され、終了したタスクだけが周回から抜けます。

```python
>>> def task(name, n):
...     for i in range(n):
...         print(name, i)
...         yield
...
>>> sched = Scheduler()
>>> sched.add(task("A", 3))
>>> sched.add(task("B", 2))
>>> sched.run()
A 0
B 0
A 1
B 1
A 2

```

実行中のタスクから新しいタスクを登録できます。

```python
>>> def parent(sched):
...     print("parent: start")
...     sched.add(child())
...     yield
...     print("parent: end")
...
>>> def child():
...     print("child: start")
...     yield
...     print("child: end")
...
>>> sched = Scheduler()
>>> sched.add(parent(sched))
>>> sched.run()
parent: start
child: start
parent: end
child: end

```

## 発展

- タスクが `yield k`（非負整数 \(k\)）と書いたら、そのタスクを \(k\) 周だけ実行せずに飛ばす簡易スリープを実装してください。
- タスク内の例外でスケジューラ全体が止まらないよう拡張し、`run()` が終了時に（タスク, 例外）の対のリストを返すようにしてください。
- `send()` を使って `yield` 式の値としてタスクへデータを渡す、タスク間のメッセージキューを設計してください。

## 参考

- 『Python Distilled』第6章「拡張ジェネレータの応用」
- 『Python Distilled』第6章「ジェネレータと非同期処理との橋渡し」
- [ノンプリエンプティブマルチタスク - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%8E%E3%83%B3%E3%83%97%E3%83%AA%E3%82%A8%E3%83%B3%E3%83%97%E3%83%86%E3%82%A3%E3%83%96%E3%83%9E%E3%83%AB%E3%83%81%E3%82%BF%E3%82%B9%E3%82%AF)
