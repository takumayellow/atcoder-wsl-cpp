# 解説スライド (Beamer) 作成ガイド

## 概要

問題の解説を Beamer (LaTeX) スライドとして作成し、PDF に出力する手順。

## ファイル構成

問題フォルダ（例: `abc303/b/`）に以下を配置する:

| ファイル | 内容 |
|---|---|
| `slides.tex` | スライド本体 |
| `latexmkrc` | latexmk 設定（platex + dvipdfmx） |
| `build_slides.ps1` | ビルドスクリプト (PowerShell) |

## テンプレート

### slides.tex の雛形

```latex
\documentclass[dvipdfmx,aspectratio=169]{beamer}
\usepackage{amsmath}
\usepackage{booktabs}
\usepackage{pxjahyper}

\usetheme{Madrid}
\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}

\title{コンテスト名 -- 問題番号\\\small サブタイトル}
\author{}
\date{}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

% スライドをここに追加

\end{document}
```

### latexmkrc

```perl
$latex = 'platex -interaction=nonstopmode -file-line-error %O %S';
$bibtex = 'pbibtex %O %S';
$dvipdf = 'dvipdfmx %O -o %D %S';
$pdf_mode = 3;
$max_repeat = 5;
$clean_ext = 'aux bbl blg dvi fls fdb_latexmk log nav out snm toc vrb';
```

## ビルド方法

PowerShell で問題フォルダに移動して実行:

```powershell
cd <contest>/<problem>
.\build_slides.ps1
```

デフォルトで `slides.tex` をビルドする。別ファイル名の場合:

```powershell
.\build_slides.ps1 -Target "other_slides.tex"
```

### 前提条件

- TeX Live 2024 がインストール済み (`C:\texlive\2024\`)
- `platex`, `dvipdfmx`, `latexmk` にパスが通っている

## スライド構成の目安

1. **タイトル**: コンテスト名・問題番号
2. **問題の概要**: 入力・出力・制約を簡潔に
3. **考察**: 解法の核心部分を段階的に説明
4. **具体例**: 小さい入力で手計算
5. **コード**: `[fragile]` オプション + `verbatim` 環境
6. **まとめ**: 覚えるべきポイント

## 注意点

- `verbatim` を使うフレームには `[fragile]` オプションが必要
- 日本語は `pxjahyper` パッケージで対応
- 中間ファイルは `build_slides.ps1` が自動削除する
