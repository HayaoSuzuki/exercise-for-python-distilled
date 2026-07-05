from references.ch04 import p0400_point_protocol as point_mod


def test_point2d_exposes_coordinates() -> None:
    # Arrange
    point = point_mod.Point2D(3, 4)

    # Act
    actual = (point.x, point.y)

    # Assert
    assert actual == (3, 4)


def test_point2d_repr_uses_class_name_and_coordinates() -> None:
    # Arrange
    point = point_mod.Point2D(3, 4)

    # Act
    actual = repr(point)

    # Assert
    assert actual == "Point2D(3, 4)"


def test_point2d_compares_equal_to_same_coordinates() -> None:
    # Arrange
    left = point_mod.Point2D(3, 4)
    right = point_mod.Point2D(3, 4)

    # Act
    actual = left == right

    # Assert
    assert actual is True


def test_point2d_does_not_compare_equal_to_tuple() -> None:
    # Arrange
    point = point_mod.Point2D(3, 4)

    # Act
    actual = point == (3, 4)

    # Assert
    assert actual is False


def test_point2d_len_returns_coordinate_count() -> None:
    # Arrange
    point = point_mod.Point2D(3, 4)

    # Act
    actual = len(point)

    # Assert
    assert actual == 2


def test_point2d_iterates_over_coordinates() -> None:
    # Arrange
    point = point_mod.Point2D(3, 4)

    # Act
    actual = tuple(point)

    # Assert
    assert actual == (3, 4)
