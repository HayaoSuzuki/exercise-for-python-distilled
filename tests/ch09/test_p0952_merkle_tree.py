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


def test_merkle_root_rejects_empty_leaves() -> None:
    # Arrange
    leaves: list[bytes] = []

    # Act
    with pytest.raises(ValueError) as exc_info:
        merkle_mod.merkle_root(leaves)

    # Assert
    assert "葉が空" in str(exc_info.value)

