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
    assert node.name == "a"


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


def test_node_cache_len_counts_cached_nodes() -> None:
    # Arrange
    cache = weak_mod.NodeCache()
    nodes = [cache.get("a"), cache.get("b")]

    # Act
    actual = len(cache)

    # Assert
    assert actual == 2
    assert [node.name for node in nodes] == ["a", "b"]


def test_node_cache_len_drops_dead_nodes() -> None:
    # Arrange
    cache = weak_mod.NodeCache()
    node = cache.get("a")
    dropped = cache.get("b")

    # Act
    del dropped
    gc.collect()

    # Assert
    assert node.name == "a"
    if sys.implementation.name == "cpython":
        assert len(cache) == 1
