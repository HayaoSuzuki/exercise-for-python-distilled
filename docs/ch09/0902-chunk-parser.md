---
title: "0902: struct によるチャンク形式のパース"
description: "タグと長さを持つチャンクの繰り返しからなるバイナリ形式を struct モジュールで解析します。"
difficulty: 3
---

# 0902: struct によるチャンク形式のパース

## 問題

PNG や RIFF（WAV、AVI）などのバイナリファイル形式は、**チャンク**（タグ、長さ、ペイロードの組）を並べた構造を採用しています。
長さがヘッダに書かれているため、パーサは未知のタグのチャンクを読み飛ばせて、形式を後方互換に拡張できます。

この構造の簡易版を解析する関数 `parse_chunks(data: bytes) -> list[tuple[bytes, bytes]]` を実装してください。
入力 `data` は 0 個以上のチャンクの連結で、各チャンクのレイアウトは次の通りです。

| フィールド | サイズ | 内容 |
| --- | --- | --- |
| タグ | 4 バイト | チャンクの種別を表すバイト列 |
| 長さ | 4 バイト | ペイロードのバイト数（ビッグエンディアンの符号なし整数） |
| ペイロード | 長さフィールドの値 | チャンク本体 |

戻り値は、出現順の `(タグ, ペイロード)` のリストです。
ヘッダの解析には `struct` モジュールを使います。

## 制約

- `data` は `bytes` です。空のバイト列に対しては空のリストを返します。
- 次の長さ不整合に対して `ValueError` を送出します。
    - チャンクヘッダの途中（8 バイト未満）でデータが尽きる
    - 長さフィールドの値に対してペイロードが足りない
- 例外メッセージは「例」に示す形式（問題箇所のバイトオフセットを含む）に合わせます。
- タグの内容は検証しません（任意の 4 バイトを許します）。

## 例

```python
>>> import struct
>>> data = struct.pack(">4sI", b"HEAD", 3) + b"abc" + struct.pack(">4sI", b"DATA", 0)
>>> parse_chunks(data)
[(b'HEAD', b'abc'), (b'DATA', b'')]
>>> parse_chunks(b"")
[]
>>> parse_chunks(struct.pack(">4sI", b"BODY", 10) + b"short")
Traceback (most recent call last):
    ...
ValueError: ペイロードが宣言された長さ 10 に足りません（位置 8）
>>> parse_chunks(data + b"TAG")
Traceback (most recent call last):
    ...
ValueError: チャンクヘッダが不完全です（位置 19）

```

## 発展

PNG の実際のチャンクは、ペイロードの後ろにタグとペイロードに対する CRC-32 検査値（4 バイト、ビッグエンディアン）を持ちます。
`zlib.crc32()` を使って検査値の検証つきパーサに拡張してください。
また、`parse_chunks()` をジェネレータ関数に書き換え、巨大な入力でもリスト全体を作らずに逐次処理できるようにしてください。

## 参考

- 『Python Distilled』第9章「I/O標準ライブラリ」の「`struct`」
- [PNG Specification: Chunk layout](https://www.w3.org/TR/png-3/#5Chunk-layout)
