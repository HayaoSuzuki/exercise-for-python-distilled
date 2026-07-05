import pytest

from references.ch09 import p0902_chunk_parser as chunks_mod


def test_parse_chunks_returns_empty_list_for_empty_data() -> None:
    # Arrange

    # Act
    actual = chunks_mod.parse_chunks(b"")

    # Assert
    assert actual == []


def test_parse_chunks_returns_tag_payload_pairs() -> None:
    # Arrange
    data = b"HEAD\x00\x00\x00\x03abcDATA\x00\x00\x00\x00"

    # Act
    actual = chunks_mod.parse_chunks(data)

    # Assert
    assert actual == [(b"HEAD", b"abc"), (b"DATA", b"")]


def test_parse_chunks_rejects_incomplete_header() -> None:
    # Arrange
    data = b"HEA"

    # Act
    with pytest.raises(ValueError) as exc_info:
        chunks_mod.parse_chunks(data)

    # Assert
    assert "チャンクヘッダが不完全" in str(exc_info.value)


def test_parse_chunks_rejects_truncated_payload() -> None:
    # Arrange
    data = b"BODY\x00\x00\x00\x0ashort"

    # Act
    with pytest.raises(ValueError) as exc_info:
        chunks_mod.parse_chunks(data)

    # Assert
    assert "ペイロード" in str(exc_info.value)

