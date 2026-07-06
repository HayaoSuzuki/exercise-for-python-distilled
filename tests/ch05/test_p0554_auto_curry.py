import pytest

from references.ch05 import p0554_auto_curry as curry_mod


@pytest.mark.parametrize(
    ("call_shape", "expected"),
    [("one_by_one", 6), ("two_then_one", 6), ("one_then_two", 6), ("all_at_once", 6)],
)
def test_curry_accepts_partial_application_shapes(call_shape: str, expected: int) -> None:
    # Arrange
    @curry_mod.curry
    def add3(x, y, z):
        return x + y + z

    # Act
    if call_shape == "one_by_one":
        actual = add3(1)(2)(3)
    elif call_shape == "two_then_one":
        actual = add3(1, 2)(3)
    elif call_shape == "one_then_two":
        actual = add3(1)(2, 3)
    else:
        actual = add3(1, 2, 3)

    # Assert
    assert actual == expected


def test_curry_reuses_partial_application_without_mutating_state() -> None:
    # Arrange
    @curry_mod.curry
    def add3(x, y, z):
        return x + y + z

    add_1_2 = add3(1, 2)

    # Act
    actual = [add_1_2(10), add_1_2(100)]

    # Assert
    assert actual == [13, 103]


def test_curry_raises_type_error_for_too_many_arguments() -> None:
    # Arrange
    @curry_mod.curry
    def add3(x, y, z):
        return x + y + z

    # Act
    with pytest.raises(TypeError) as exc_info:
        add3(1, 2, 3, 4)

    # Assert
    assert exc_info.type is TypeError


def test_curry_rejects_zero_argument_function() -> None:
    # Arrange
    def f():
        return 1

    # Act
    with pytest.raises(TypeError) as exc_info:
        curry_mod.curry(f)

    # Assert
    assert str(exc_info.value) == "curry() requires at least one positional parameter"


@pytest.mark.parametrize(
    "f",
    [
        pytest.param(lambda *, x: x, id="keyword_only_parameter"),
        pytest.param(lambda x=1: x, id="positional_parameter_with_default"),
    ],
)
def test_curry_rejects_non_required_positional_parameters(f) -> None:
    # Arrange

    # Act
    with pytest.raises(TypeError) as exc_info:
        curry_mod.curry(f)

    # Assert
    assert str(exc_info.value) == "curry() supports required positional parameters only"
