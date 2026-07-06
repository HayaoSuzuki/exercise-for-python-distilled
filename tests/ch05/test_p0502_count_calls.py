from references.ch05 import p0502_count_calls as count_mod


def test_count_calls_starts_at_zero() -> None:
    # Arrange
    def double(x: int) -> int:
        return x * 2

    # Act
    counted = count_mod.count_calls(double)

    # Assert
    assert counted.calls == 0


def test_count_calls_forwards_arguments_and_return_value() -> None:
    # Arrange
    def add(x: int, y: int) -> int:
        return x + y
    counted = count_mod.count_calls(add)

    # Act
    actual = counted(2, 3)

    # Assert
    assert actual == 5


def test_count_calls_forwards_keyword_arguments() -> None:
    # Arrange
    def greet(name: str, *, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}"
    counted = count_mod.count_calls(greet)

    # Act
    actual = counted("Bob", greeting="Hi")

    # Assert
    assert actual == "Hi, Bob"


def test_count_calls_increments_after_each_call() -> None:
    # Arrange
    def double(x: int) -> int:
        return x * 2
    counted = count_mod.count_calls(double)

    # Act
    counted(2)
    counted(4)

    # Assert
    assert counted.calls == 2


def test_count_calls_preserves_function_name() -> None:
    # Arrange
    def double(x: int) -> int:
        return x * 2

    # Act
    counted = count_mod.count_calls(double)

    # Assert
    assert counted.__name__ == "double"
