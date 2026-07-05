---
title: "0250: 内包表記で作る関係代数"
description: "辞書のリストで表した関係に対する選択・射影・自然結合を内包表記で実装します。"
difficulty: 3
---

# 0250: 内包表記で作る関係代数

## 問題

リレーショナルデータベースの理論的基礎である関係代数を、Python の組み込みデータ構造の上に実装します。
関係（relation）は「同じキー集合を持つ辞書のリスト」で表します。
辞書1つが行、キーが属性名に対応します。

次の3つの関数を実装してください。

- `select(rel, pred)` — 選択 \(\sigma_{\mathrm{pred}}(rel)\)。述語 `pred`（行を受け取って真偽値を返す呼び出し可能オブジェクト）を満たす行だけからなる関係を、元の順序を保って返します。
- `project(rel, attrs)` — 射影 \(\pi_{attrs}(rel)\)。各行を属性名の列 `attrs` に制限した関係を返します。結果の各辞書のキーは `attrs` の順に並べ、重複する行は最初の出現だけを残します。
- `natural_join(r, s)` — 自然結合 \(r \bowtie s\)。共通属性の値がすべて一致する `r` の行と `s` の行の組を1つの辞書に合成した関係を返します。行の順序は「`r` の各行について `s` を先頭から走査する」順とし、合成した辞書のキーは `r` の属性の後に `s` 固有の属性が続く順とします。

## 制約

- 関係は空でない辞書のリストであり、同じ関係に属する行はすべて同じキー集合を持ちます。属性名は文字列、値はハッシュ可能なオブジェクトです。
- いずれの関数も新しいリストを返し、引数の関係を変更してはいけません。
- `project` は、`attrs` に関係に存在しない属性名が含まれる場合、`KeyError` を送出します。
- `natural_join` は、共通属性が存在しない場合は直積を返します。
- 繰り返しはすべて内包表記（またはジェネレータ式）で書き、明示的な `for` 文・`while` 文を使わないでください。

## 例

```python
>>> students = [
...     {"sid": 1, "name": "Asa"},
...     {"sid": 2, "name": "Ume"},
... ]
>>> enrolls = [
...     {"sid": 1, "course": "Math"},
...     {"sid": 1, "course": "CS"},
...     {"sid": 2, "course": "Math"},
... ]
>>> select(enrolls, lambda t: t["course"] == "Math")
[{'sid': 1, 'course': 'Math'}, {'sid': 2, 'course': 'Math'}]
>>> project(enrolls, ["course"])
[{'course': 'Math'}, {'course': 'CS'}]
>>> natural_join(students, enrolls)
[{'sid': 1, 'name': 'Asa', 'course': 'Math'}, {'sid': 1, 'name': 'Asa', 'course': 'CS'}, {'sid': 2, 'name': 'Ume', 'course': 'Math'}]
>>> project(select(natural_join(students, enrolls), lambda t: t["course"] == "Math"), ["name"])
[{'name': 'Asa'}, {'name': 'Ume'}]
>>> project(students, ["gpa"])
Traceback (most recent call last):
    ...
KeyError: 'gpa'

```

## 発展

- 属性名を付け替える `rename(rel, mapping)` を追加し、自己結合（例: 従業員関係から「従業員とその上司」の組を求めるクエリ）が書けることを確かめてください。
- 選択と射影の順序を交換できる条件を考え、順序の交換によって中間結果が小さくなるクエリの例を作ってください。

## 参考

- 『Python Distilled』第2章「内包表記」
- 『Python Distilled』第2章「マッピング（辞書）」
- [関係代数（関係モデル） - Wikipedia](https://ja.wikipedia.org/wiki/関係代数_(関係モデル))
