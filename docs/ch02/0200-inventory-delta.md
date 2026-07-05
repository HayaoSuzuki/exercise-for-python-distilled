---
title: "0200: 在庫差分"
description: "2つの辞書を比べ、品目ごとの増減を計算します。"
difficulty: 2
---

# 0200: 在庫差分

## 問題

在庫数を表す2つの辞書 `before` と `after` から、品目ごとの増減を求める関数 `inventory_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]` を実装してください。
返り値は、`after` の数量から `before` の数量を引いた値を持つ辞書です。
増減がない品目は返り値に含めません。

## 制約

- `before` と `after` のキーは品目名、値は在庫数です。
- 片方の辞書にだけ存在する品目は、もう片方では数量 0 とみなします。
- 返り値のキーは辞書順に並べます。
- 入力の辞書を変更してはいけません。

## 例

```python
>>> inventory_delta({}, {})
{}
>>> inventory_delta({"apple": 3, "book": 1}, {"apple": 5, "pen": 2})
{'apple': 2, 'book': -1, 'pen': 2}
>>> inventory_delta({"tea": 4}, {"tea": 4})
{}
>>> inventory_delta({}, {"tea": 4})
{'tea': 4}

```

## 発展

増加した品目と減少した品目を別々の辞書に分けて返す関数を書いてください。

## 参考

- 『Python Distilled』第2章「標準的な演算子」
- 『Python Distilled』第2章「集合」
- 『Python Distilled』第2章「マッピング（辞書）」
- 『Python Distilled』第2章「内包表記」
