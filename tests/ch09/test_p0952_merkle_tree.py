import hashlib

import pytest

from references.ch09 import p0952_merkle_tree as merkle_mod

PROOF_FOR_TX4 = [
    ("R", "41b637cfd9eb3e2f60f734f9ca44e5c1559c6f481d49d6ed6891f3e9a086ac78"),
    ("R", "58d38b66050691641038c0c04b79e0c67bb34a96a8b37a7c5b502e828ef8592e"),
    ("L", "9db19fd4038d720fb19dec0f50cd6afbafe918851ddbb718773abff9783faeb0"),
]
ROOT_FOR_FIVE_LEAVES = "16eef23ee6e2c2a9a42a944da0f25b543af1d834b60e594d60c417ed4e38cb1a"


def test_merkle_root_returns_leaf_hash_for_single_leaf() -> None:
    # Arrange
    leaves = [b"a"]

    # Act
    actual = merkle_mod.merkle_root(leaves)

    # Assert
    assert actual == "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb"


def test_merkle_root_combines_pairs_for_two_leaves() -> None:
    # Arrange
    leaves = [b"a", b"b"]
    expected = hashlib.sha256(
        hashlib.sha256(b"a").digest() + hashlib.sha256(b"b").digest()
    ).hexdigest()

    # Act
    actual = merkle_mod.merkle_root(leaves)

    # Assert
    assert actual == expected


def test_merkle_root_pads_odd_levels_for_five_leaves() -> None:
    # Arrange
    leaves = [b"tx0", b"tx1", b"tx2", b"tx3", b"tx4"]

    # Act
    actual = merkle_mod.merkle_root(leaves)

    # Assert
    assert actual == ROOT_FOR_FIVE_LEAVES


def test_merkle_proof_returns_path_for_leaf_index() -> None:
    # Arrange
    leaves = [b"tx0", b"tx1", b"tx2", b"tx3", b"tx4"]

    # Act
    actual = merkle_mod.merkle_proof(leaves, 4)

    # Assert
    assert actual == PROOF_FOR_TX4


def test_merkle_verify_accepts_valid_proof() -> None:
    # Arrange

    # Act
    actual = merkle_mod.verify(b"tx4", PROOF_FOR_TX4, ROOT_FOR_FIVE_LEAVES)

    # Assert
    assert actual is True


def test_merkle_verify_rejects_wrong_leaf() -> None:
    # Arrange

    # Act
    actual = merkle_mod.verify(b"tx5", PROOF_FOR_TX4, ROOT_FOR_FIVE_LEAVES)

    # Assert
    assert actual is False


def test_merkle_verify_rejects_unknown_side_marker() -> None:
    # Arrange
    proof = [("X", "41b637cfd9eb3e2f60f734f9ca44e5c1559c6f481d49d6ed6891f3e9a086ac78")]

    # Act
    actual = merkle_mod.verify(b"tx4", proof, ROOT_FOR_FIVE_LEAVES)

    # Assert
    assert actual is False


def test_merkle_verify_rejects_malformed_hex_digest() -> None:
    # Arrange
    proof = [("L", "not hex")]

    # Act
    actual = merkle_mod.verify(b"tx4", proof, ROOT_FOR_FIVE_LEAVES)

    # Assert
    assert actual is False


def test_merkle_verify_rejects_wrong_length_sibling_digest() -> None:
    # Arrange
    # 長さ検査を外すと検証が通ってしまう root をあえて与え、検査の有無を判別する。
    short_sibling = bytes.fromhex("aa")
    root = hashlib.sha256(short_sibling + hashlib.sha256(b"tx4").digest()).hexdigest()
    proof = [("L", "aa")]

    # Act
    actual = merkle_mod.verify(b"tx4", proof, root)

    # Assert
    assert actual is False


def test_merkle_proof_accepts_lower_bound_index() -> None:
    # Arrange
    leaves = [b"tx0", b"tx1", b"tx2", b"tx3", b"tx4"]

    # Act
    proof = merkle_mod.merkle_proof(leaves, 0)

    # Assert
    assert merkle_mod.verify(leaves[0], proof, ROOT_FOR_FIVE_LEAVES) is True


@pytest.mark.parametrize("index", [-1, 5])
def test_merkle_proof_rejects_out_of_range_index(index: int) -> None:
    # Arrange
    leaves = [b"tx0", b"tx1", b"tx2", b"tx3", b"tx4"]

    # Act
    with pytest.raises(IndexError) as exc_info:
        merkle_mod.merkle_proof(leaves, index)

    # Assert
    assert str(exc_info.value) == f"葉の添字 {index} が範囲外です"


def test_merkle_root_rejects_empty_leaves() -> None:
    # Arrange
    leaves: list[bytes] = []

    # Act
    with pytest.raises(ValueError) as exc_info:
        merkle_mod.merkle_root(leaves)

    # Assert
    assert str(exc_info.value) == "葉が空です"

