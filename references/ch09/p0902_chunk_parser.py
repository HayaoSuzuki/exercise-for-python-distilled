"""0902: struct によるチャンク形式のパースのリファレンス実装。"""

import struct

_HEADER = struct.Struct(">4sI")


def parse_chunks(data: bytes) -> list[tuple[bytes, bytes]]:
    chunks: list[tuple[bytes, bytes]] = []
    offset = 0
    n = len(data)
    while offset < n:
        if n - offset < _HEADER.size:
            raise ValueError(f"チャンクヘッダが不完全です（位置 {offset}）")
        tag, length = _HEADER.unpack_from(data, offset)
        offset += _HEADER.size
        if n - offset < length:
            raise ValueError(f"ペイロードが宣言された長さ {length} に足りません（位置 {offset}）")
        chunks.append((tag, data[offset : offset + length]))
        offset += length
    return chunks
