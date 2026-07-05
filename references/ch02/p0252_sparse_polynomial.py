"""0252: 辞書で表す疎多項式（リファレンス実装）。"""

Poly = dict[int, int]


def poly_add(p: Poly, q: Poly) -> Poly:
    """多項式の和 p + q を返す。ゼロ係数の項は含めない。"""
    sums = {k: p.get(k, 0) + q.get(k, 0) for k in p.keys() | q.keys()}
    return {k: c for k, c in sums.items() if c != 0}


def poly_mul(p: Poly, q: Poly) -> Poly:
    """多項式の積 pq を畳み込みで計算して返す。ゼロ係数の項は含めない。"""
    prod: Poly = {}
    for i, a in p.items():
        for j, b in q.items():
            prod[i + j] = prod.get(i + j, 0) + a * b
    return {k: c for k, c in prod.items() if c != 0}


def poly_eval(p: Poly, x: complex) -> complex:
    """多項式 p の x における値を返す。ゼロ多項式には 0 を返す。"""
    return sum(c * x**k for k, c in p.items())
