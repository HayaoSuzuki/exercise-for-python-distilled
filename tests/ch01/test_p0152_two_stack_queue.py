import pytest

from references.ch01 import p0152_two_stack_queue as queue_mod


def test_queue_dequeues_items_in_fifo_order() -> None:
    # Arrange
    queue = queue_mod.Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Act
    actual = [queue.dequeue(), queue.dequeue(), queue.dequeue()]

    # Assert
    assert actual == [1, 2, 3]


def test_queue_len_reports_remaining_items() -> None:
    # Arrange
    queue = queue_mod.Queue[str]()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.dequeue()

    # Act
    actual = len(queue)

    # Assert
    assert actual == 1


def test_queue_dequeue_raises_index_error_when_empty() -> None:
    # Arrange
    queue = queue_mod.Queue[int]()

    # Act
    with pytest.raises(IndexError) as exc_info:
        queue.dequeue()

    # Assert
    assert str(exc_info.value) == "dequeue from empty queue"
