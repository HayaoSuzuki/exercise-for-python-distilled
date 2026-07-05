"""0302: 例外の連鎖を保つ再帰下降パーサ のリファレンス実装。"""


class ParseError(Exception):
    """式の解析または評価の失敗を表す例外。"""


def _tokenize(src: str) -> list[str]:
    tokens: list[str] = []
    i = 0
    while i < len(src):
        ch = src[i]
        if ch.isspace():
            i += 1
        elif ch in "0123456789":
            j = i
            while j < len(src) and src[j] in "0123456789":
                j += 1
            tokens.append(src[i:j])
            i = j
        elif ch in "+-*/()":
            tokens.append(ch)
            i += 1
        else:
            raise ParseError(f"invalid character: {ch!r}")
    return tokens


class _Parser:
    def __init__(self, tokens: list[str]) -> None:
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> str | None:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self) -> str:
        current = self.peek()
        if current is None:
            raise ParseError("unexpected end of input")
        self.pos += 1
        return current

    def expr(self) -> int | float:
        value = self.term()
        while self.peek() in ("+", "-"):
            op = self.advance()
            right = self.term()
            value = value + right if op == "+" else value - right
        return value

    def term(self) -> int | float:
        value = self.factor()
        while self.peek() in ("*", "/"):
            op = self.advance()
            right = self.factor()
            if op == "*":
                value = value * right
            else:
                try:
                    value = value / right
                except ZeroDivisionError as exc:
                    raise ParseError("division by zero") from exc
        return value

    def factor(self) -> int | float:
        current = self.peek()
        if current is None:
            raise ParseError("unexpected end of input")
        if current == "(":
            self.advance()
            value = self.expr()
            if self.peek() != ")":
                raise ParseError("expected ')'")
            self.advance()
            return value
        if current.isdigit():
            self.advance()
            return int(current)
        raise ParseError(f"unexpected token: {current!r}")


def evaluate(src: str) -> int | float:
    """四則演算と括弧からなる式文字列を評価する。"""
    parser = _Parser(_tokenize(src))
    value = parser.expr()
    if parser.peek() is not None:
        raise ParseError(f"unexpected token: {parser.peek()!r}")
    return value
