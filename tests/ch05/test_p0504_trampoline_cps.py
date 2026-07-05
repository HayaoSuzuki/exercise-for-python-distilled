from references.ch05 import p0504_trampoline_cps as tramp_mod


def test_trampoline_returns_final_non_callable_value() -> None:
    # Arrange
    def immediate() -> int:
        return 42

    # Act
    actual = tramp_mod.trampoline(immediate)

    # Assert
    assert actual == 42


def test_trampoline_runs_deep_tail_call_chain() -> None:
    # Arrange
    def sum_to(n: int, acc: int = 0):
        if n == 0:
            return acc
        return lambda: sum_to(n - 1, acc + n)

    # Act
    actual = tramp_mod.trampoline(sum_to, 1000)

    # Assert
    assert actual == 500500
