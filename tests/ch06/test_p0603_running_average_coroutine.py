from references.ch06 import p0603_running_average_coroutine as average_mod


def test_running_average_next_primes_generator() -> None:
    # Arrange
    average = average_mod.running_average()

    # Act
    actual = next(average)

    # Assert
    assert actual is None


def test_running_average_returns_first_value_as_average() -> None:
    # Arrange
    average = average_mod.running_average()
    next(average)

    # Act
    actual = average.send(10.0)

    # Assert
    assert actual == 10.0


def test_running_average_updates_average_after_multiple_values() -> None:
    # Arrange
    average = average_mod.running_average()
    next(average)

    # Act
    average.send(10.0)
    actual = average.send(20.0)

    # Assert
    assert actual == 15.0


def test_running_average_send_none_keeps_current_average() -> None:
    # Arrange
    average = average_mod.running_average()
    next(average)
    average.send(10.0)

    # Act
    actual = average.send(None)

    # Assert
    assert actual == 10.0
