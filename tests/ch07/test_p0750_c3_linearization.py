import pytest

from references.ch07 import p0750_c3_linearization as c3_mod


def test_c3_linearization_matches_python_mro_for_simple_graph() -> None:
    # Arrange
    graph = {"object": [], "X": ["object"], "Y": ["object"], "A": ["X", "Y"]}

    class X:
        pass

    class Y:
        pass

    class A(X, Y):
        pass

    # Act
    actual = c3_mod.linearize("A", graph)

    # Assert
    assert actual == ["A", "X", "Y", "object"]


def test_c3_linearization_raises_type_error_for_inconsistent_order() -> None:
    # Arrange
    graph = {
        "object": [],
        "X": ["object"],
        "Y": ["object"],
        "A": ["X", "Y"],
        "B": ["Y", "X"],
        "Z": ["A", "B"],
    }

    # Act
    with pytest.raises(TypeError) as exc_info:
        c3_mod.linearize("Z", graph)

    # Assert
    assert str(exc_info.value) == "Cannot create a consistent method resolution order (MRO) for Z"


def test_c3_linearization_raises_type_error_for_direct_cycle() -> None:
    # Arrange
    graph = {"A": ["B"], "B": ["A"]}

    # Act
    with pytest.raises(TypeError) as exc_info:
        c3_mod.linearize("A", graph)

    # Assert
    assert str(exc_info.value) == "Cannot create a consistent method resolution order (MRO) for A"
