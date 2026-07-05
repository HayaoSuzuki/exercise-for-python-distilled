import pytest

from references.ch04 import p0453_lazy_attribute as lazy_mod


@pytest.mark.parametrize(("attribute", "expected"), [("total", 14), ("minimum", 1), ("maximum", 5)])
def test_lazy_stats_computes_attribute_on_first_access(attribute: str, expected: int) -> None:
    # Arrange
    stats = lazy_mod.LazyStats([3, 1, 4, 1, 5])

    # Act
    actual = getattr(stats, attribute)

    # Assert
    assert actual == expected


def test_lazy_stats_reuses_cached_attribute_value() -> None:
    # Arrange
    stats = lazy_mod.LazyStats([3, 1, 4, 1, 5])

    # Act
    _ = stats.total
    _ = stats.total
    actual = stats.computations

    # Assert
    assert actual == 1
