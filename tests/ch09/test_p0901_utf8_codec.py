import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch09 import p0901_utf8_codec as utf8_mod
from tests._helpers import FAST


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", b""),
        ("ASCII", b"ASCII"),
        ("π", b"\xcf\x80"),
        ("🐍", b"\xf0\x9f\x90\x8d"),
        ("Aπ🐍", b"A\xcf\x80\xf0\x9f\x90\x8d"),
    ],
)
def test_utf8_encode_returns_expected_bytes(text: str, expected: bytes) -> None:
    # Arrange

    # Act
    actual = utf8_mod.utf8_encode(text)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        (b"", ""),
        (b"ASCII", "ASCII"),
        (b"\xcf\x80", "π"),
        (b"\xf0\x9f\x90\x8d", "🐍"),
        (b"A\xcf\x80\xf0\x9f\x90\x8d", "Aπ🐍"),
    ],
)
def test_utf8_decode_returns_expected_text(data: bytes, expected: str) -> None:
    # Arrange

    # Act
    actual = utf8_mod.utf8_decode(data)

    # Assert
    assert actual == expected


@FAST
@given(st.text(alphabet=st.characters(blacklist_categories=("Cs",)), max_size=50))
def test_utf8_encode_matches_builtin_for_valid_text(text: str) -> None:
    # Arrange

    # Act
    actual = utf8_mod.utf8_encode(text)

    # Assert
    assert actual == text.encode("utf-8")


@FAST
@given(st.text(alphabet=st.characters(blacklist_categories=("Cs",)), max_size=50))
def test_utf8_decode_matches_builtin_for_valid_bytes(text: str) -> None:
    # Arrange
    data = text.encode("utf-8")

    # Act
    actual = utf8_mod.utf8_decode(data)

    # Assert
    assert actual == text


@pytest.mark.parametrize(
    ("data", "expected_message"),
    [
        (b"\x80", "不正な先頭バイト"),
        (b"\xc0\x80", "overlong encoding"),
        (b"\xe2\x28\xa1", "不正な継続バイト"),
        (b"\xf0\x9f\x90", "継続バイトが不足"),
    ],
)
def test_utf8_decode_rejects_invalid_sequences(data: bytes, expected_message: str) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        utf8_mod.utf8_decode(data)

    # Assert
    assert expected_message in str(exc_info.value)


def test_utf8_encode_rejects_surrogate_code_point() -> None:
    # Arrange
    text = "\ud800"

    # Act
    with pytest.raises(ValueError) as exc_info:
        utf8_mod.utf8_encode(text)

    # Assert
    assert "サロゲート" in str(exc_info.value)

