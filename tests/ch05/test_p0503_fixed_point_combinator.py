from references.ch05 import p0503_fixed_point_combinator as fix_mod


def test_fix_builds_recursive_factorial() -> None:
    # Arrange
    factorial = fix_mod.fix(lambda rec: lambda n: 1 if n == 0 else n * rec(n - 1))

    # Act
    actual = factorial(6)

    # Assert
    assert actual == 720
