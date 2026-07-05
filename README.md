# exercise-for-python-distilled

『Python Distilled』のための演習問題

『Python Distilled』の各章の内容をベースに、計算機科学および数学の問題を作成しました。

## セットアップ

```
uv sync
```

## プレビュー

```
uv run mkdocs serve
```

## ビルド

```
uv run mkdocs build --strict
```

## 検証

問題ページの doctest 形式の「例」を、`references/` の検証専用実装（サイトには公開されない）に対して実行します。

```
uv run python tools/check_doctests.py
```

## 執筆規約

- 1問1ページ。ファイル名は `docs/chCC/CCNN-slug.md`（`CC`=章番号2桁、`NN`=章内番号2桁）
- front matter に `title` / `description` / `difficulty`（3〜5）を書く。難易度は内部データであり本文・一覧には表示しない
- 見出しは `## 問題` → `## 制約` → `## 例`（doctest 形式）、必要に応じて `## 発展` `## 参考`
- `## 参考` に『Python Distilled』の対応節を明記する
- 各問題に対応する検証用実装を `references/chCC/pCCNN_slug.py` に置く
- 雛形は `templates/problem.md`
