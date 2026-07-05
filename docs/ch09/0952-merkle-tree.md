---
title: "0952: hashlib で作る Merkle 木"
description: "SHA-256 で Merkle 木を構成し、認証パスによる包含証明と検証を実装します。"
difficulty: 4
---

# 0952: hashlib で作る Merkle 木

## 問題

**Merkle 木**は、データ列のハッシュ値を二分木状に畳み込んだ構造です。
根のハッシュ値（Merkle 根）を 1 つ知っていれば、「ある葉が列に含まれること」を木の高さぶんのハッシュ値（**認証パス**）だけで検証できます。
Git のオブジェクトストアやブロックチェーン、証明書透明性ログの改竄検出に使われています。

`hashlib.sha256()` を使い、次の 3 つの関数を実装してください。

- `merkle_root(leaves: list[bytes]) -> str`：Merkle 根の 16 進表現を返します。
- `merkle_proof(leaves: list[bytes], index: int) -> list[tuple[str, str]]`：`leaves[index]` の認証パスを返します。
- `verify(leaf: bytes, proof: list[tuple[str, str]], root: str) -> bool`：認証パス `proof` を使って、`leaf` が根 `root` の木に含まれるかを判定します。

木の構成規則は次の通りです。
ここで \(H(x)\) は SHA-256 のダイジェスト（32 バイト）を表します。

1. 第 0 段は葉のハッシュ値の列 \([H(\ell_0), H(\ell_1), \dots]\) とします。
2. ある段の要素数が奇数なら、最後の要素を複製して偶数にします。
3. 次の段は、隣接する 2 要素を左から順に連結してハッシュした列 \([H(h_0 \| h_1), H(h_2 \| h_3), \dots]\) とします。
4. 要素が 1 つになるまで 2〜3 を繰り返し、残った 1 つを根とします。

認証パスは、葉から根へ向かう各段での「相手側のハッシュ値」の列です。
各要素は `(側, 16進ハッシュ値)` の組で、側は相手が左隣なら `"L"`、右隣なら `"R"` とします。

## 制約

- 葉は `bytes` の列です。`merkle_root()` と `merkle_proof()` は、葉が空の場合に `ValueError` を送出します。
- `merkle_proof()` は、`index` が範囲外の場合に `IndexError` を送出します。
- 葉が 1 つの木の根は \(H(\ell_0)\) で、その認証パスは空のリストです。
- `verify()` は `leaves` を受け取らずに、`leaf`、`proof`、`root` だけから判定します。

## 例

```python
>>> merkle_root([b"a"])
'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb'
>>> merkle_root([b"tx0", b"tx1", b"tx2"])
'726da7d399987671da491c4886e07dacd532fb6e7e48862732701d2443e3b532'
>>> leaves = [b"tx0", b"tx1", b"tx2", b"tx3", b"tx4"]
>>> root = merkle_root(leaves)
>>> proof = merkle_proof(leaves, 4)
>>> len(proof)
3
>>> verify(b"tx4", proof, root)
True
>>> verify(b"tx5", proof, root)
False
>>> verify(b"a", merkle_proof([b"a"], 0), merkle_root([b"a"]))
True
>>> merkle_root([])
Traceback (most recent call last):
    ...
ValueError: 葉が空です

```

## 発展

この構成には、葉のハッシュ値と内部節点のハッシュ値を区別しないことに起因する**第二原像攻撃**（内部節点の値を葉として提示すると、異なる列が同じ根を持つ）が知られています。
葉には `H(b"\x00" + データ)`、内部節点には `H(b"\x01" + 左 + 右)` とドメイン分離した版を実装し、攻撃が成立しなくなることを確かめてください。

## 参考

- 『Python Distilled』第9章「I/O標準ライブラリ」の「`hashlib`」
- [Merkle tree - Wikipedia](https://en.wikipedia.org/wiki/Merkle_tree)
