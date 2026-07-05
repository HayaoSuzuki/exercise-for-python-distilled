from references.ch07 import p0703_hash_consing as intern_mod


def test_intern_meta_reuses_instance_for_same_class_and_args() -> None:
    # Arrange
    class Symbol(metaclass=intern_mod.InternMeta):
        def __init__(self, name):
            self.name = name

    # Act
    first = Symbol("x")
    second = Symbol("x")

    # Assert
    assert first is second


def test_intern_meta_keeps_tables_separate_per_class() -> None:
    # Arrange
    class Symbol(metaclass=intern_mod.InternMeta):
        def __init__(self, name):
            self.name = name

    class OtherSymbol(metaclass=intern_mod.InternMeta):
        def __init__(self, name):
            self.name = name

    # Act
    symbol = Symbol("x")
    other_symbol = OtherSymbol("x")

    # Assert
    assert symbol is not other_symbol
