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


def test_disjoint_set_accepts_zero_size() -> None:
    # Arrange

    # Act
    disjoint_set = uf_mod.DisjointSet(0)

    # Assert
    assert disjoint_set.count == 0


def test_disjoint_set_rejects_negative_size() -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        uf_mod.DisjointSet(-1)

    # Assert
    assert str(exc_info.value) == "n must be non-negative"


def test_disjoint_set_union_returns_whether_a_merge_happened() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(2)

    # Act
    first = disjoint_set.union(0, 1)
    second = disjoint_set.union(0, 1)

    # Assert
    assert first is True
    assert second is False


def test_disjoint_set_find_compresses_a_two_level_chain() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(4)
    disjoint_set.union(0, 1)
    disjoint_set.union(2, 3)
    disjoint_set.union(1, 3)

    # Act
    actual = disjoint_set.find(3)

    # Assert
    assert actual == 0
    # 圧縮は戻り値に現れないため、親配列が根へ張り替わったことを直接確かめる。
    assert disjoint_set._parent[3] == 0  # noqa: SLF001


def test_disjoint_set_union_uses_rank_to_choose_new_root() -> None:
    # Arrange
    disjoint_set = uf_mod.DisjointSet(8)
    disjoint_set.union(0, 1)
    disjoint_set.union(4, 5)
    disjoint_set.union(6, 7)
    disjoint_set.union(4, 6)

    # Act
    actual = disjoint_set.union(0, 4)

    # Assert
    assert actual is True
    assert disjoint_set.find(0) == 4


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
