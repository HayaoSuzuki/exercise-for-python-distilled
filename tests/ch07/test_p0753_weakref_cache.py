import gc
import sys

from references.ch07 import p0753_weakref_cache as weak_mod


def test_node_cache_reuses_live_node() -> None:
    # Arrange
    cache = weak_mod.NodeCache()
    node = cache.get("a")

    # Act
    actual = cache.get("a")

    # Assert
    assert actual is node


def test_node_cache_drops_entry_after_last_strong_reference_disappears() -> None:
    # Arrange
    cache = weak_mod.NodeCache()
    node = cache.get("a")

    # Act
    del node
    gc.collect()

    # Assert
    if sys.implementation.name == "cpython":
        assert "a" not in cache
