from references.ch04 import p0402_multiset_order as multiset_mod


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
