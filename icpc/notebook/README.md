# notebook/ — 印刷用チームノート

本番はネット不可なので、`library/` を **A4 に印刷して持ち込む**。ここはその PDF を作る場所。

## いちばん簡単な作り方（pandoc）

`library/` のソースを 1 つの Markdown にまとめて PDF 化する:

```bash
# 例: cpp と py をまとめて 1 冊に
{
  echo '# ICPC Team Notebook'
  for f in ../library/cpp/*.hpp ../library/py/*.py; do
    echo; echo "## $(basename "$f")"; echo '```'; cat "$f"; echo '```'
  done
} > notebook.md

pandoc notebook.md -o notebook.pdf \
  --pdf-engine=lualatex -V documentclass=ltjarticle -V geometry:margin=15mm
```

> 日本語コメントを含むので `lualatex` + `ltjarticle`（または `xelatex` + CJK フォント）推奨。
> ない場合は VSCode で Markdown を開いて「印刷」→ PDF でも可。

## abc462/c のスライドパイプラインを流用する場合

`abc462/c` に `slides.tex` ビルドがある。同じ仕組みでコード集を組版したいときはそれを土台に
`notebook.tex` を作る（TODO: 必要になったら整備）。当面は上の pandoc 一発で十分。

## 印刷前チェック
- [ ] 1 スニペット = なるべく 1 ページ内（途中改ページで貼りミスを防ぐ）
- [ ] フォントは等幅・行番号なし（貼り付け時に混入しない）
- [ ] ACL 抜粋は `namespace atcoder { ... }` ごと載っているか
