"""0950: UTF-8 コーデックの手書き実装のリファレンス実装。"""

_MIN_CODEPOINT = {2: 0x80, 3: 0x800, 4: 0x10000}


def utf8_encode(s: str) -> bytes:
    out = bytearray()
    for i, ch in enumerate(s):
        cp = ord(ch)
        if 0xD800 <= cp <= 0xDFFF:
            raise ValueError(f"サロゲート U+{cp:04X} はエンコードできません（位置 {i}）")
        if cp < 0x80:
            out.append(cp)
        elif cp < 0x800:
            out.append(0xC0 | (cp >> 6))
            out.append(0x80 | (cp & 0x3F))
        elif cp < 0x10000:
            out.append(0xE0 | (cp >> 12))
            out.append(0x80 | ((cp >> 6) & 0x3F))
            out.append(0x80 | (cp & 0x3F))
        else:
            out.append(0xF0 | (cp >> 18))
            out.append(0x80 | ((cp >> 12) & 0x3F))
            out.append(0x80 | ((cp >> 6) & 0x3F))
            out.append(0x80 | (cp & 0x3F))
    return bytes(out)


def utf8_decode(b: bytes) -> str:
    chars: list[str] = []
    i = 0
    n = len(b)
    while i < n:
        lead = b[i]
        if lead < 0x80:
            chars.append(chr(lead))
            i += 1
            continue
        if lead >> 5 == 0b110:
            length, cp = 2, lead & 0x1F
        elif lead >> 4 == 0b1110:
            length, cp = 3, lead & 0x0F
        elif lead >> 3 == 0b11110:
            length, cp = 4, lead & 0x07
        else:
            raise ValueError(f"不正な先頭バイト 0x{lead:02X}（位置 {i}）")
        if i + length > n:
            raise ValueError(f"継続バイトが不足しています（位置 {i}）")
        for j in range(i + 1, i + length):
            byte = b[j]
            if byte >> 6 != 0b10:
                raise ValueError(f"不正な継続バイト 0x{byte:02X}（位置 {j}）")
            cp = (cp << 6) | (byte & 0x3F)
        if cp < _MIN_CODEPOINT[length]:
            raise ValueError(f"overlong encoding（位置 {i}）")
        if 0xD800 <= cp <= 0xDFFF:
            raise ValueError(f"サロゲート U+{cp:04X} はデコードできません（位置 {i}）")
        if cp > 0x10FFFF:
            raise ValueError(f"Unicode の範囲外の符号位置（位置 {i}）")
        chars.append(chr(cp))
        i += length
    return "".join(chars)
