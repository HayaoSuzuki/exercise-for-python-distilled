---
title: "1051: 3引数 pow による Miller–Rabin"
description: "3引数の pow と divmod だけを道具に、Miller–Rabin の確率的素数判定を決定的な底の集合で実装します。"
difficulty: 4
---

# 1051: 3引数 pow による Miller–Rabin

## 問題

奇数 \(n \ge 3\) に対して \(n - 1 = 2^s d\)（\(d\) は奇数）と分解すると、\(n\) が素数ならば、\(n\) と互いに素な任意の底 \(a\) について

\[
a^d \equiv 1 \pmod n
\quad\text{または}\quad
a^{2^r d} \equiv -1 \pmod n \ (0 \le r < s)
\]

のいずれかが成り立ちます。
どちらも成り立たない底 \(a\) が見つかれば、\(n\) は合成数だと確定します（このような \(a\) を**証人**と呼びます）。
逆にある底でこの条件を満たしてしまう合成数を、その底に対する**強擬素数**と呼びます。
これが Miller–Rabin 素数判定法です。

関数 `is_probable_prime(n, bases=None)` を実装してください。
`bases` で与えた各底について上の判定を行い、すべての底で合成数と判定されなければ `True` を返します。
この `True` は「与えた底では合成数の証人が見つからなかった」という意味です。
任意の `bases` を渡した場合、数学的な素数性を常に保証する値ではありません。
`bases` が `None` のときは既定の底の集合 \(\{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37\}\) を使います。
この集合は \(n < 3{,}317{,}044{,}064{,}679{,}887{,}385{,}961{,}981\) の範囲で判定を決定的にする（強擬素数が存在しない）ことが知られています。

## 制約

- `n` は整数です。整数でない引数には `TypeError` を送出します。
- `n < 2`（負の数を含む）に対しては `False` を返します。
- 冪剰余は必ず3引数の `pow(base, exp, mod)` で計算します。`**` や2引数の `pow` で巨大な冪を作ってはいけません。
- \(n - 1 = 2^s d\) の分解には `divmod` を使います。
- `math` モジュールを含め、モジュールのインポートは行いません。組み込み関数だけで実装します。
- 底 `a` が `n` の倍数のときは、その底を判定に使わず読み飛ばします。
- 読み飛ばした結果、調べる底が1つも残らない場合も `True` を返します。
- `bases` には整数のイテラブルが渡されます。

## 例

```python
>>> is_probable_prime(2)
True
>>> is_probable_prime(1)
False
>>> is_probable_prime(-7)
False
>>> [n for n in range(2, 40) if is_probable_prime(n)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
>>> is_probable_prime(561)  # カーマイケル数 561 = 3 * 11 * 17
False
>>> is_probable_prime(2**61 - 1)  # メルセンヌ素数
True
>>> is_probable_prime(2**61 + 1)
False
>>> is_probable_prime(2047)  # 2047 = 23 * 89
False
>>> is_probable_prime(2047, bases=(2,))  # 底 2 に対する最小の強擬素数
True
>>> is_probable_prime(9, bases=(9, 2))  # 9 は読み飛ばし、2 で合成数とわかる
False
>>> is_probable_prime(9, bases=(9,))  # 調べる底が残らない
True
>>> is_probable_prime(3.0)
Traceback (most recent call last):
  ...
TypeError: n must be an int

```

## 発展

Fermat の小定理に基づく素朴な判定（\(a^{n-1} \equiv 1 \pmod n\) の確認だけ）を `is_fermat_probable_prime(n, bases)` として実装し、カーマイケル数 561, 1105, 1729 に対して、`n` と互いに素な底をいくつ試しても合成数と見抜けないことを確かめてください。
Miller–Rabin が同じ底でこれらを合成数と判定できる理由を、\(x^2 \equiv 1 \pmod n\) の非自明な平方根と関連づけて説明してください。

## 参考

- 『Python Distilled』第10章「組み込み関数」
- [ミラー–ラビン素数判定法 - Wikipedia](https://ja.wikipedia.org/wiki/%E3%83%9F%E3%83%A9%E3%83%BC%E2%80%93%E3%83%A9%E3%83%93%E3%83%B3%E7%B4%A0%E6%95%B0%E5%88%A4%E5%AE%9A%E6%B3%95)
