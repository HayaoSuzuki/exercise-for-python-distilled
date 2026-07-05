"""0650: 無限素数ストリーム（増分エラトステネス篩）。"""

from __future__ import annotations

from collections.abc import Iterator


def primes() -> Iterator[int]:
    """素数を小さい順に無限に生成する。

    合成数をキー、その合成数を割り切ると判明している素数のリストを
    値とする辞書だけを内部状態に持つ増分篩。素数 p は p * p が候補に
    到達するまで辞書に現れないため、辞書サイズは pi(sqrt(n)) 程度に収まる。
    """
    factors: dict[int, list[int]] = {}
    n = 2
    while True:
        if n in factors:
            # n は合成数。篩を素数ごとに次の倍数へ進める。
            for p in factors.pop(n):
                factors.setdefault(n + p, []).append(p)
        else:
            # n は素数。最初に篩い落とすべき倍数は n * n。
            yield n
            factors[n * n] = [n]
        n += 1
