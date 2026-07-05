---
title: "0950: UTF-8 コーデックの手書き実装"
description: "UTF-8 の可変長符号化をビット演算だけで実装し、不正なバイト列の検出まで行います。"
difficulty: 4
---

# 0950: UTF-8 コーデックの手書き実装

## 問題

UTF-8 は、Unicode の符号位置を 1〜4 バイトの可変長で表す接頭符号です。
どのバイトも先頭ビットのパターンから「1 バイト文字」「先頭バイト」「継続バイト」のいずれかを判別できるため、途中のバイトから読み始めても文字境界に復帰できます（自己同期符号）。

この符号化を自分の手で実装します。
次の 2 つの関数を書いてください。

- `utf8_encode(s: str) -> bytes`：文字列を UTF-8 のバイト列に変換します。
- `utf8_decode(b: bytes) -> str`：UTF-8 のバイト列を文字列に変換します。

符号位置 \(c\) とバイト列の対応は次の表の通りです。
`x` の部分に \(c\) の 2 進表現を上位ビットから詰めます。

| 符号位置の範囲 | バイト列のビットパターン |
| --- | --- |
| U+0000 〜 U+007F | `0xxxxxxx` |
| U+0080 〜 U+07FF | `110xxxxx 10xxxxxx` |
| U+0800 〜 U+FFFF | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000 〜 U+10FFFF | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

各符号位置は、この表の中で最短のバイト列で符号化しなければなりません。
必要以上に長い表現（**overlong encoding**。たとえば `/` U+002F を 2 バイトの `0xC0 0xAF` で表したもの）は不正なバイト列です。

## 制約

- `utf8_encode()` と `utf8_decode()` の内部では、`str.encode()`、`bytes.decode()`、`codecs` モジュールを使ってはいけません。変換は `ord()`、`chr()` とビット演算で行います。
- `utf8_decode()` は、次の不正なバイト列に対して `ValueError` を送出します。
    - 先頭バイトとして現れてはならないバイト（`10xxxxxx` や `0xF8` 以上）
    - 先頭バイトが要求する数の継続バイトがない、または継続バイトの位置に `10xxxxxx` 以外のバイトがある
    - overlong encoding
    - サロゲート（U+D800 〜 U+DFFF）や U+10FFFF を超える値を表すバイト列
- `utf8_encode()` は、文字列にサロゲートが含まれる場合に `ValueError` を送出します。
- 例外メッセージは「例」に示す形式（問題箇所のバイトオフセットまたは文字位置を含む）に合わせます。

## 例

```python
>>> utf8_encode("Aπ🐍")
b'A\xcf\x80\xf0\x9f\x90\x8d'
>>> utf8_decode(b'A\xcf\x80\xf0\x9f\x90\x8d')
'Aπ🐍'
>>> s = "".join(chr(c) for c in [0x7F, 0x80, 0x7FF, 0x800, 0xFFFF, 0x10000, 0x10FFFF])
>>> utf8_encode(s) == s.encode("utf-8")
True
>>> utf8_decode(utf8_encode(s)) == s
True
>>> utf8_encode("\ud800")
Traceback (most recent call last):
    ...
ValueError: サロゲート U+D800 はエンコードできません（位置 0）
>>> utf8_decode(b"\xc0\xaf")
Traceback (most recent call last):
    ...
ValueError: overlong encoding（位置 0）
>>> utf8_decode(b"A\xe3\x81")
Traceback (most recent call last):
    ...
ValueError: 継続バイトが不足しています（位置 1）
>>> utf8_decode(b"\xed\xa0\x80")
Traceback (most recent call last):
    ...
ValueError: サロゲート U+D800 はデコードできません（位置 0）

```

## 発展

バイト列の任意の位置 \(i\) を受け取り、\(i\) 以降で最初の文字境界を返す関数 `resync(b, i)` を書き、UTF-8 が自己同期符号であることを確かめてください。
また、`utf8_decode()` に `errors="replace"` 相当のモード（不正なバイト列を U+FFFD に置換して続行する）を追加してください。

## 参考

- 『Python Distilled』第9章「テキストのエンコードとデコード」
- [RFC 3629: UTF-8, a transformation format of ISO 10646](https://www.rfc-editor.org/rfc/rfc3629)
