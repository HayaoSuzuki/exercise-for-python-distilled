import pytest

from references.ch02 import p0201_relational_algebra as rel


def test_project_removes_duplicate_rows_preserving_first_occurrence() -> None:
    # Arrange
    rows = [
        {"sid": 1, "course": "Math"},
        {"sid": 1, "course": "CS"},
        {"sid": 2, "course": "Math"},
    ]

    # Act
    actual = rel.project(rows, ["course"])

    # Assert
    assert actual == [{"course": "Math"}, {"course": "CS"}]


def test_select_preserves_matching_rows_in_input_order() -> None:
    # Arrange
    rows = [
        {"sid": 1, "course": "Math"},
        {"sid": 1, "course": "CS"},
        {"sid": 2, "course": "Math"},
    ]

    # Act
    actual = rel.select(rows, lambda row: row["course"] == "Math")

    # Assert
    assert actual == [{"sid": 1, "course": "Math"}, {"sid": 2, "course": "Math"}]


def test_natural_join_combines_rows_with_matching_common_attributes() -> None:
    # Arrange
    students = [{"sid": 1, "name": "Asa"}, {"sid": 2, "name": "Ume"}]
    enrolls = [
        {"sid": 1, "course": "Math"},
        {"sid": 1, "course": "CS"},
        {"sid": 2, "course": "Math"},
    ]

    # Act
    actual = rel.natural_join(students, enrolls)

    # Assert
    assert actual == [
        {"sid": 1, "name": "Asa", "course": "Math"},
        {"sid": 1, "name": "Asa", "course": "CS"},
        {"sid": 2, "name": "Ume", "course": "Math"},
    ]


@pytest.mark.parametrize(("left", "right"), [([], [{"sid": 1}]), ([{"sid": 1}], [])])
def test_natural_join_returns_empty_list_when_either_relation_is_empty(
    left: list[dict[str, int]], right: list[dict[str, int]]
) -> None:
    # Arrange

    # Act
    actual = rel.natural_join(left, right)

    # Assert
    assert actual == []

