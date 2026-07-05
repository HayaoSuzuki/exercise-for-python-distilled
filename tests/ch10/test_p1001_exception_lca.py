from typing import Any, cast

import pytest

from references.ch10 import p1001_exception_lca as lca_mod


@pytest.mark.parametrize(
    ("exc_types", "expected"),
    [
        ((FileNotFoundError, PermissionError), OSError),
        ((KeyError, UnicodeDecodeError), Exception),
        ((ValueError, KeyboardInterrupt), BaseException),
        ((LookupError,), LookupError),
    ],
)
def test_common_handler_returns_nearest_common_exception_base(
    exc_types: tuple[type[BaseException], ...], expected: type[BaseException]
) -> None:
    # Arrange

    # Act
    actual = lca_mod.common_handler(*exc_types)

    # Assert
    assert actual is expected


def test_common_handler_rejects_empty_input() -> None:
    # Arrange

    # Act
    with pytest.raises(TypeError) as exc_info:
        lca_mod.common_handler()

    # Assert
    assert "at least one exception class" in str(exc_info.value)


def test_common_handler_rejects_non_exception_class() -> None:
    # Arrange
    exc_type = cast("Any", int)

    # Act
    with pytest.raises(TypeError) as exc_info:
        lca_mod.common_handler(exc_type)

    # Assert
    assert "is not an exception class" in str(exc_info.value)
