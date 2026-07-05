import pytest

from references.ch07 import p0702_history_stack as stack_mod


def test_history_stack_starts_empty() -> None:
    # Arrange

    # Act
    stack = stack_mod.HistoryStack()

    # Assert
    assert len(stack) == 0


def test_history_stack_push_adds_item() -> None:
    # Arrange
    stack = stack_mod.HistoryStack()

    # Act
    stack.push("a")

    # Assert
    assert list(stack) == ["a"]


def test_history_stack_pop_returns_last_item() -> None:
    # Arrange
    stack = stack_mod.HistoryStack()
    stack.push("a")
    stack.push("b")

    # Act
    actual = stack.pop()

    # Assert
    assert actual == "b"


def test_history_stack_records_history() -> None:
    # Arrange
    stack = stack_mod.HistoryStack()

    # Act
    stack.push("a")
    stack.push("b")
    stack.pop()

    # Assert
    assert stack.history == [("push", "a"), ("push", "b"), ("pop", "b")]


def test_history_stack_rejects_pop_from_empty_stack() -> None:
    # Arrange
    stack = stack_mod.HistoryStack()

    # Act
    with pytest.raises(IndexError) as exc_info:
        stack.pop()

    # Assert
    assert str(exc_info.value) == "pop from empty stack"
