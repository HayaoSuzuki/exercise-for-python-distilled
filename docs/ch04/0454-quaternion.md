---
title: "0454: 四元数"
description: "非可換な積を持つ四元数を数値プロトコルで実装し、__mul__ と __rmul__ の役割分担を扱う問題です。"
difficulty: 4
---

# 0454: 四元数

## 問題

四元数 \(q = a + bi + cj + dk\) を表すクラス `Quaternion` を実装してください。
四元数は乗法が可換でない斜体をなし、3D 回転の表現に使われます。

基底 \(i, j, k\) は次の関係を満たします。

\[
i^2 = j^2 = k^2 = ijk = -1
\]

この関係から、積は次のように定まります。

\[
\begin{aligned}
q_1 q_2 = {}& (a_1 a_2 - b_1 b_2 - c_1 c_2 - d_1 d_2) \\
&+ (a_1 b_2 + b_1 a_2 + c_1 d_2 - d_1 c_2)\,i \\
&+ (a_1 c_2 - b_1 d_2 + c_1 a_2 + d_1 b_2)\,j \\
&+ (a_1 d_2 + b_1 c_2 - c_1 b_2 + d_1 a_2)\,k
\end{aligned}
\]

`Quaternion(a, b, c, d)` は成分 \(a, b, c, d\) の四元数を表します。
次のメソッドを実装します。

- `__add__`：四元数同士の成分ごとの和。
- `__mul__`：上式による四元数同士の積。オペランドがスカラー（`int` または `Fraction`）の場合はスカラー倍。
- `__rmul__`：`2 * q` のような左からのスカラー倍。
- `__abs__`：ノルム \(\sqrt{a^2 + b^2 + c^2 + d^2}\) を `float` で返します。
- `__eq__`：4 成分がすべて等しいときに限り `True` を返します。
- `__repr__`：`eval()` で再作成できる `Quaternion(1, -2, 3, 0)` の形式を返します。
- `conjugate()`：共役 \(\bar{q} = a - bi - cj - dk\) を返します。
- `inverse()`：乗法逆元 \(q^{-1} = \bar{q} / (a^2 + b^2 + c^2 + d^2)\) を返します。

積が非可換であること（`i * j` と `j * i` が異なること）を「例」で確認します。

## 制約

- 成分は `int` または `fractions.Fraction` に限ります。それ以外の成分は `TypeError` を送出します（`float` は許しません）。
- 分母が 1 の `Fraction` 成分は `int` に正規化し、`repr` の出力を安定させます。
- スカラー倍のスカラーも `int` または `Fraction` に限ります。
- 四元数と `Quaternion` 以外のオブジェクトとの `+` や `==` では `NotImplemented` を返します。
- 零四元数の `inverse()` は、メッセージ `zero quaternion has no inverse` の `ZeroDivisionError` を送出します。

## 例

```python
>>> from fractions import Fraction
>>> i = Quaternion(0, 1, 0, 0)
>>> j = Quaternion(0, 0, 1, 0)
>>> k = Quaternion(0, 0, 0, 1)
>>> i * i
Quaternion(-1, 0, 0, 0)
>>> i * j
Quaternion(0, 0, 0, 1)
>>> j * i
Quaternion(0, 0, 0, -1)
>>> i * j == j * i
False
>>> i * j == k
True
>>> q = Quaternion(1, 2, 3, 4)
>>> q + Quaternion(4, 3, 2, 1)
Quaternion(5, 5, 5, 5)
>>> 2 * q
Quaternion(2, 4, 6, 8)
>>> Fraction(1, 2) * q
Quaternion(Fraction(1, 2), 1, Fraction(3, 2), 2)
>>> q.conjugate()
Quaternion(1, -2, -3, -4)
>>> abs(Quaternion(1, 1, 1, 1))
2.0
>>> q.inverse()
Quaternion(Fraction(1, 30), Fraction(-1, 15), Fraction(-1, 10), Fraction(-2, 15))
>>> q * q.inverse()
Quaternion(1, 0, 0, 0)
>>> Quaternion(0, 0, 0, 0).inverse()
Traceback (most recent call last):
  ...
ZeroDivisionError: zero quaternion has no inverse

```

## 発展

- `__sub__` と単項の `__neg__` を追加してください。
- `__truediv__` を `q1 * q2.inverse()` として定義してください。積が非可換なので、「右から割る」と「左から割る」が異なることを例で確認してください。
- 単位四元数 \(q\) による回転 \(v \mapsto q v q^{-1}\) を実装し、\(q = \frac{1}{\sqrt{2}}(1 + i)\) に相当する回転が \(y\) 軸を \(z\) 軸に写すことを確認してください（ノルムが無理数にならないよう、係数のかけ方を工夫します）。

## 参考

- 『Python Distilled』第4章「数値プロトコル」
- 『Python Distilled』第4章「プロトコルとデータの抽象化」
- [四元数 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%9B%9B%E5%85%83%E6%95%B0)
