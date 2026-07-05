import pytest

from references.ch07 import p0755_slots_union_find as uf_mod


def test_disjoint_set_union_connects_components() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(5)

    # Act
    disjoint_set.union(0, 1)
    disjoint_set.union(1, 2)
    actual = disjoint_set.connected(0, 2)

    # Assert
    assert actual is True


def test_disjoint_set_count_decreases_after_successful_unions() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(5)

    # Act
    disjoint_set.union(0, 1)
    disjoint_set.union(1, 2)

    # Assert
    assert disjoint_set.count == 3


def test_disjoint_set_instances_do_not_have_dict() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(5)

    # Act
    actual = hasattr(disjoint_set, "__dict__")

    # Assert
    assert actual is False


def test_disjoint_set_find_rejects_out_of_range_element() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(5)

    # Act
    with pytest.raises(IndexError) as exc_info:
        disjoint_set.find(5)

    # Assert
    assert "element 5 is out of range" in str(exc_info.value)
