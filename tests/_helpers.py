from hypothesis import settings

FAST = settings(max_examples=60, deadline=None)


def brute_inversions(seq: list[int]) -> int:
    return sum(1 for i, x in enumerate(seq) for y in seq[i + 1 :] if x > y)


def simple_is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def assert_valid_queens(solution: list[int], n: int) -> None:
    assert len(solution) == n
    assert sorted(solution) == list(range(n))
    assert len({r + c for r, c in enumerate(solution)}) == n
    assert len({r - c for r, c in enumerate(solution)}) == n
