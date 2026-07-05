"""問題ページの doctest を references/ の実装で検証する。

docs/chCC/CCNN-slug.md の ```python ブロックから doctest を抽出し、
references/chCC/pCCNN_slug.py をロードした名前空間で実行する。
"""

from __future__ import annotations

import doctest
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REFERENCES = ROOT / "references"

FENCE_RE = re.compile(r"^```python\s*\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)


def reference_path(problem_md: Path) -> Path:
    chapter = problem_md.parent.name
    module = "p" + problem_md.stem.replace("-", "_")
    return REFERENCES / chapter / f"{module}.py"


def check_problem(problem_md: Path) -> tuple[int, int]:
    """（失敗数, 実行数）を返す。"""
    rel = problem_md.relative_to(ROOT)
    parser = doctest.DocTestParser()
    examples = [
        example
        for block in FENCE_RE.findall(problem_md.read_text(encoding="utf-8"))
        for example in parser.get_examples(block)
    ]
    if not examples:
        print(f"[warn] {rel}: doctest の例がありません")
        return 0, 0

    ref = reference_path(problem_md)
    if not ref.exists():
        print(f"[fail] {rel}: リファレンス実装 {ref.relative_to(ROOT)} がありません")
        return 1, len(examples)

    namespace: dict = {"__name__": ref.stem}
    exec(compile(ref.read_text(encoding="utf-8"), str(ref), "exec"), namespace)

    test = doctest.DocTest(
        examples, namespace, name=str(rel), filename=str(problem_md), lineno=0, docstring=None
    )
    runner = doctest.DocTestRunner(optionflags=doctest.ELLIPSIS)
    result = runner.run(test)
    return result.failed, result.attempted


def main(chapters: list[str] | None = None) -> int:
    problems = sorted(DOCS.glob("ch[0-9][0-9]/[0-9][0-9][0-9][0-9]-*.md"))
    if chapters:
        problems = [p for p in problems if p.parent.name in chapters]
    if not problems:
        print("問題ページが見つかりません")
        return 1

    total_failed = total_attempted = failed_files = 0
    for problem_md in problems:
        failed, attempted = check_problem(problem_md)
        total_failed += failed
        total_attempted += attempted
        if failed:
            failed_files += 1

    print(
        f"{len(problems)} ファイル / {total_attempted} 例を検証、"
        f"失敗 {total_failed} 例（{failed_files} ファイル）"
    )
    return 1 if total_failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
