import pytest

from references.ch04 import p0452_cons_list as cons_mod


def test_cons_list_iterates_from_head_to_tail() -> None:
    # Arrange
    items = cons_mod.ConsList().cons(3).cons(2).cons(1)

    # Act
    actual = list(items)

    # Assert
    assert actual == [1, 2, 3]


def test_cons_list_preserves_tail_for_structure_sharing() -> None:
    # Arrange
    tail = cons_mod.ConsList().cons("b")

    # Act
    items = tail.cons("a")

    # Assert
    assert items.tail is tail


def test_cons_list_rejects_attribute_assignment_after_creation() -> None:
    # Arrange
    items = cons_mod.ConsList().cons(1)

    # Act
    with pytest.raises(AttributeError) as exc_info:
        type(items).__setattr__(items, "head", 99)

    # Assert
    assert "ConsList is immutable" in str(exc_info.value)


def test_cons_list_rejects_attribute_deletion_after_creation() -> None:
    # Arrange
    items = cons_mod.ConsList().cons(1)

    # Act
    with pytest.raises(AttributeError) as exc_info:
        del items.head

    # Assert
    assert str(exc_info.value) == "ConsList is immutable"


def test_cons_list_len_reflects_number_of_cons_calls() -> None:
    # Arrange
    items = cons_mod.ConsList().cons(1).cons(2).cons(3)

    # Act
    actual = len(items)

    # Assert
    assert actual == 3


@pytest.mark.parametrize(("item", "expected"), [(3, True), (2, True), (1, True), (99, False)])
def test_cons_list_contains_checks_membership(item: int, expected: bool) -> None:
    # Arrange
    items = cons_mod.ConsList().cons(3).cons(2).cons(1)

    # Act
    actual = item in items

    # Assert
    assert actual is expected


@pytest.mark.parametrize(("index", "expected"), [(0, 1), (1, 2), (2, 3)])
def test_cons_list_getitem_returns_value_at_index(index: int, expected: int) -> None:
    # Arrange
    items = cons_mod.ConsList().cons(3).cons(2).cons(1)

    # Act
    actual = items[index]

    # Assert
    assert actual == expected


def test_cons_list_getitem_rejects_non_int_index() -> None:
    # Arrange
    items = cons_mod.ConsList().cons(3).cons(2).cons(1)

    # Act
    with pytest.raises(TypeError) as exc_info:
        items["0"]  # type: ignore[index]  # ty:ignore[invalid-argument-type]

    # Assert
    assert str(exc_info.value) == "ConsList indices must be integers"


@pytest.mark.parametrize("index", [-1, 3])
def test_cons_list_getitem_rejects_index_out_of_range(index: int) -> None:
    # Arrange
    items = cons_mod.ConsList().cons(3).cons(2).cons(1)

    # Act
    with pytest.raises(IndexError) as exc_info:
        items[index]

    # Assert
    assert str(exc_info.value) == "ConsList index out of range"
