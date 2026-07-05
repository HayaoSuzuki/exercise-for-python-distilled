from references.ch05 import p0503_shared_default as tag_mod


def test_add_tag_returns_singleton_list_when_tags_are_omitted() -> None:
    # Arrange

    # Act
    actual = tag_mod.add_tag("python")

    # Assert
    assert actual == ["python"]


def test_add_tag_does_not_share_omitted_tags_between_calls() -> None:
    # Arrange

    # Act
    first = tag_mod.add_tag("python")
    second = tag_mod.add_tag("distilled")

    # Assert
    assert first is not second


def test_add_tag_appends_to_existing_tags_in_return_value() -> None:
    # Arrange
    tags = ["book"]

    # Act
    actual = tag_mod.add_tag("python", tags)

    # Assert
    assert actual == ["book", "python"]


def test_add_tag_does_not_modify_existing_tags() -> None:
    # Arrange
    tags = ["book"]

    # Act
    tag_mod.add_tag("python", tags)

    # Assert
    assert tags == ["book"]
