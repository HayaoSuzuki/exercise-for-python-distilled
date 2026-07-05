---
title: "0751: ディスクリプタで作る単位付き量"
description: "属性への代入時に物理量の次元を検査するデータディスクリプタを実装します。"
difficulty: 4
---

# 0751: ディスクリプタで作る単位付き量

## 問題

物理量は数値と**次元**の組で表せます。
基本単位を長さ、質量、時間の 3 つとすると、任意の単位はその指数の組 \((e_L, e_M, e_T)\) で表せます。
例えば長さは \((1, 0, 0)\)、速度（\(\mathrm{m/s}\)）は \((1, 0, -1)\) です。
量の乗除は指数の加減に対応するので、次元の全体は自由アーベル群 \(\mathbb{Z}^3\) をなします。
この表現を使うと、次元の合わない値の代入を型エラーとして検出できます。

次の 2 つのクラスを実装してください。

- `Quantity(value, dim)`:数値 `value` と次元 `dim`（整数のタプル）を属性に持つクラス。`repr()` は `Quantity(3.0, (1, 0, 0))` の形式とする。
- `Measured(dim)`:次元 `dim` の量だけを受け付けるデータディスクリプタ。
    - `__set_name__()` で、クラス内で束縛された属性名を記録する。
    - `__set__()` は、値が `Quantity` でなければ `TypeError`（メッセージは `<属性名> expects a Quantity, got <型名>`）を、次元が `dim` と一致しなければ `TypeError`（メッセージは `<属性名> expects dimension <dim>, got <実際の次元>`）を送出する。検査に通った値はインスタンスの `__dict__` に属性名をキーとして格納する。
    - `__get__()` は、インスタンス経由の参照では格納された値を、クラス経由の参照ではディスクリプタ自身を返す。

## 制約

- `dim` は int のタプルで、次元の比較はタプルの等価比較で行います。
- `Measured` はクラスレベルでのみ使われます。
- `property` や `__setattr__` の再定義で代用してはいけません。

## 例

```python
>>> LENGTH = (1, 0, 0)     #（長さ, 質量, 時間）の指数
>>> VELOCITY = (1, 0, -1)  # m/s
>>> class Particle:
...     position = Measured(LENGTH)
...     velocity = Measured(VELOCITY)
...     def __init__(self, position, velocity):
...         self.position = position
...         self.velocity = velocity
...
>>> p = Particle(Quantity(3.0, LENGTH), Quantity(1.5, VELOCITY))
>>> p.position
Quantity(3.0, (1, 0, 0))
>>> p.velocity = Quantity(2.0, VELOCITY)   # 次元が合うので代入できる
>>> p.velocity.value
2.0
>>> p.velocity = Quantity(2.0, (0, 0, 1))  # 時間の量は速度に代入できない
Traceback (most recent call last):
    ...
TypeError: velocity expects dimension (1, 0, -1), got (0, 0, 1)
>>> p.position = 3.0
Traceback (most recent call last):
    ...
TypeError: position expects a Quantity, got float
>>> Particle.position is Particle.__dict__["position"]
True

```

## 発展

`Quantity` に乗算と除算を実装してください。
数値部分は通常どおり乗除し、次元は指数ベクトルの加算（除算では減算）で合成します。
`Quantity(3.0, LENGTH) / Quantity(1.5, VELOCITY)` が時間の次元 \((0, 0, 1)\) を持つことを確認してください。

## 参考

- 『Python Distilled』第7章「ディスクリプタ」
- [次元解析 - Wikipedia](https://ja.wikipedia.org/wiki/次元解析)
