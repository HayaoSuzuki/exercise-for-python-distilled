import pytest

from references.ch04 import p0451_multiset_order as multiset_mod


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        (multiset_mod.Multiset("aab"), multiset_mod.Multiset("aab"), True),
        (multiset_mod.Multiset("aab"), multiset_mod.Multiset("aabb"), False),
        (multiset_mod.Multiset("a"), "a", False),
    ],
)
def test_multiset_eq_compares_counts_and_rejects_other_types(
    left: multiset_mod.Multiset, right: object, expected: bool
) -> None:
    # Arrange

    # Act
    actual = left == right

    # Assert
    assert actual is expected


def test_multiset_subset_comparison_returns_true_for_proper_subset() -> None:
    # Arrange
    subset = multiset_mod.Multiset("aab")
    superset = multiset_mod.Multiset("aabb")

    # Act
    actual = subset < superset

    # Assert
    assert actual is True


def test_multiset_reflected_comparison_uses_subset_relation() -> None:
    # Arrange
    subset = multiset_mod.Multiset("aab")
    superset = multiset_mod.Multiset("aabb")

    # Act
    actual = superset >= subset

    # Assert
    assert actual is True


def test_multiset_incomparable_pair_is_not_ordered() -> None:
    # Arrange
    left = multiset_mod.Multiset("aab")
    right = multiset_mod.Multiset("abc")

    # Act
    actual = left <= right or right <= left

    # Assert
    assert actual is False


def test_multiset_strict_subset_comparison_is_false_for_equal_multisets() -> None:
    # Arrange
    left = multiset_mod.Multiset("aab")
    right = multiset_mod.Multiset("aab")

    # Act
    actual = left < right

    # Assert
    assert actual is False
