---
title: "1050: 例外階層の最近共通祖先"
description: "except 節のマッチング規則を根拠に、複数の例外クラスをまとめて捕捉できる最も特殊な基底クラスを __mro__ から求めます。"
difficulty: 3
---

# 1050: 例外階層の最近共通祖先

## 問題

`except C:` という節は、送出された例外が `C` のインスタンス、すなわち `C` またはその派生クラスのインスタンスであるときにマッチします。
したがって、複数種類の例外を一つの `except` 節で捕捉したいときは、それらの共通の基底クラスを指定すれば足ります。
組み込み例外は `BaseException` を根とする木構造をなすので、「与えられた例外クラスをすべて捕捉でき、その中で最も特殊なクラス」は木構造でいう**最近共通祖先**（lowest common ancestor）です。

関数 `common_handler(*exc_types)` を実装してください。
1個以上の例外クラスを受け取り、そのすべてを1つの `except` 節で捕捉できるクラスのうち、継承の木で最も深いものを返します。
各クラスの継承関係は `__mro__` 属性から読み取ります。

## 制約

- 引数はそれぞれ `BaseException` またはその派生クラスです。
- 例外クラスでない引数（例外クラスのインスタンスや、`BaseException` を継承しないクラスを含む）が1つでもあれば `TypeError` を送出します。
- 引数が0個の場合も `TypeError` を送出します。
- `Exception` 系と `SystemExit` や `KeyboardInterrupt` などの `BaseException` 直下の系統が混在する場合も正しく扱います。
- 組み込み例外と同様の単一継承の木構造を仮定してかまいません。

## 例

```python
>>> common_handler(FileNotFoundError, PermissionError)
<class 'OSError'>
>>> common_handler(IndexError, KeyError)
<class 'LookupError'>
>>> common_handler(ZeroDivisionError, OverflowError)
<class 'ArithmeticError'>
>>> common_handler(KeyError, UnicodeDecodeError)
<class 'Exception'>
>>> common_handler(ValueError, KeyboardInterrupt)
<class 'BaseException'>
>>> common_handler(FileNotFoundError)
<class 'FileNotFoundError'>
>>> common_handler(int, str)
Traceback (most recent call last):
  ...
TypeError: <class 'int'> is not an exception class
>>> common_handler()
Traceback (most recent call last):
  ...
TypeError: at least one exception class is required

```

## 発展

多重継承された例外クラスでは最近共通祖先が一意に決まるとは限りません。
`OSError` と `ValueError` の両方を継承したユーザ定義例外を2つ作り、`common_handler` が何を返すかを確かめてください。
その返り値が引数の並び順に依存するかどうかも調べ、`__mro__` の線形化がこの問題にどう関わるかを説明してください。

## 参考

- 『Python Distilled』第10章「組み込み例外」
- 『Python Distilled』第10章「基底例外クラス」
- 『Python Distilled』第10章「組み込み例外クラス」
- [最小共通祖先 - Wikipedia](https://ja.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E5%85%B1%E9%80%9A%E7%A5%96%E5%85%88)
