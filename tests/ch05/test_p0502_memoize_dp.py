from references.ch05 import p0502_memoize_dp as memo_mod


def test_memoize_returns_cached_value_on_second_call() -> None:
    # Arrange
    calls = {"count": 0}

    @memo_mod.memoize
    def square(x: int) -> int:
        calls["count"] += 1
        return x * x

    # Act
    square(4)
    actual = square(4)

    # Assert
    assert actual == 16


def test_memoize_skips_function_body_for_cached_argument() -> None:
    # Arrange
    calls = {"count": 0}

    @memo_mod.memoize
    def square(x: int) -> int:
        calls["count"] += 1
        return x * x

    # Act
    square(4)
    square(4)

    # Assert
    assert calls == {"count": 1}


def test_memoize_preserves_wrapped_function_name() -> None:
    # Arrange
    @memo_mod.memoize
    def square(x: int) -> int:
        return x * x

    # Act
    actual = square.__name__

    # Assert
    assert actual == "square"
