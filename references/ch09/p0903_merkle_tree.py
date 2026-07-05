"""0903: hashlib で作る Merkle 木のリファレンス実装。"""

import hashlib


def _hash(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def _leaf_level(leaves: list[bytes]) -> list[bytes]:
    if not leaves:
        raise ValueError("葉が空です")
    return [_hash(leaf) for leaf in leaves]


def merkle_root(leaves: list[bytes]) -> str:
    level = _leaf_level(leaves)
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [_hash(level[i] + level[i + 1]) for i in range(0, len(level), 2)]
    return level[0].hex()


def merkle_proof(leaves: list[bytes], index: int) -> list[tuple[str, str]]:
    level = _leaf_level(leaves)
    if not 0 <= index < len(leaves):
        raise IndexError(f"葉の添字 {index} が範囲外です")
    proof: list[tuple[str, str]] = []
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        sibling = index ^ 1
        side = "L" if sibling < index else "R"
        proof.append((side, level[sibling].hex()))
        level = [_hash(level[i] + level[i + 1]) for i in range(0, len(level), 2)]
        index //= 2
    return proof


def verify(leaf: bytes, proof: list[tuple[str, str]], root: str) -> bool:
    h = _hash(leaf)
    for side, sibling_hex in proof:
        if side not in {"L", "R"}:
            return False
        try:
            sibling = bytes.fromhex(sibling_hex)
        except ValueError:
            return False
        if len(sibling) != hashlib.sha256().digest_size:
            return False
        h = _hash(sibling + h) if side == "L" else _hash(h + sibling)
    return h.hex() == root
