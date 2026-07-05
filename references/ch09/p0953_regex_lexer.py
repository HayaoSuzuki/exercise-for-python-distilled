"""0953: re で作る字句解析器のリファレンス実装。"""

import re

_TOKEN_SPEC = [
    ("NUMBER", r"\d+(?:\.\d+)?"),
    ("NAME", r"[A-Za-z_][A-Za-z0-9_]*"),
    ("OP", r"==|!=|<=|>=|[+\-*/=<>()]"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
    ("MISMATCH", r"."),
]
_PATTERN = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in _TOKEN_SPEC))


def tokenize(src: str) -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    line = 1
    line_start = 0
    for m in _PATTERN.finditer(src):
        kind = m.lastgroup
        if kind is None:
            raise RuntimeError("token kind is unavailable")
        text = m.group()
        if kind == "NEWLINE":
            line += 1
            line_start = m.end()
        elif kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            column = m.start() - line_start + 1
            raise SyntaxError(f"{line}行{column}列: 予期しない文字 {text!r}")
        else:
            tokens.append((kind, text))
    return tokens
