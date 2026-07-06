import statistics
from typing import cast

from references.ch06 import p0652_online_variance as stats_mod


def test_stats_next_primes_generator() -> None:
    # Arrange
    stats = stats_mod.stats()

    # Act
    actual = next(stats)

    # Assert
    assert actual is None


def test_stats_returns_count_mean_and_population_variance() -> None:
    # Arrange
    stats = stats_mod.stats()
    next(stats)

    # Act
    actual = [stats.send(0.0), stats.send(3.0), stats.send(6.0)]

    # Assert
    assert actual == [(1, 0.0, 0.0), (2, 1.5, 2.25), (3, 3.0, 6.0)]


def test_stats_initial_mean_is_zero_for_huge_first_value() -> None:
    # Arrange
    stats = stats_mod.stats()
    next(stats)
    x = 9007199254740994.0  # 2**53 + 2

    # Act
    actual = stats.send(x)

    # Assert
    assert actual == (1, 9007199254740994.0, 0.0)


def test_stats_variance_matches_statistics_pvariance() -> None:
    # Arrange
    data = [0.5 * k for k in range(1, 101)]
    stats = stats_mod.stats()
    next(stats)

    # Act
    actual = 0.0
    for value in data:
        _, _, actual = cast("stats_mod.Result", stats.send(value))

    # Assert
    assert round(actual, 10) == round(statistics.pvariance(data), 10)
