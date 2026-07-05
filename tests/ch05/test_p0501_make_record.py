from typing import Any

import pytest

from references.ch05 import p0501_make_record as record_mod


def test_make_record_returns_required_fields() -> None:
    # Arrange

    # Act
    actual = record_mod.make_record("Ada")

    # Assert
    assert actual == {"name": "Ada", "tags": (), "active": True}


def test_make_record_collects_tags_active_flag_and_attrs() -> None:
    # Arrange

    # Act
    actual = record_mod.make_record("Ada", "math", "python", active=False, score=10)

    # Assert
    assert actual == {"name": "Ada", "tags": ("math", "python"), "active": False, "score": 10}


@pytest.mark.parametrize("reserved_key", ["name", "tags"])
def test_make_record_rejects_reserved_attrs(reserved_key: str) -> None:
    # Arrange
    attrs: dict[str, Any] = {reserved_key: "override"}

    # Act
    with pytest.raises(ValueError) as exc_info:
        record_mod.make_record("Ada", **attrs)

    # Assert
    assert str(exc_info.value) == f"reserved attribute: {reserved_key}"
