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
