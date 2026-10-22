# 解説スライド (Beamer) 作成ガイド

`explanation.md` を書いた問題を、図つきのスライド (PDF) に再構成する手順。
正本はあくまで Markdown の [`explanation.md`](explanation_guide.md)。
**スライドは「考察を図で見せる版」であって、別に考察を書き直すものではない。**

## 作り方（3 ステップ）

```bash
# 1. 雛形を作る（slides.tex + latexmkrc。タイトルは contest.acc.json から自動で埋まる）
cd abc128/c
../../tools/new_slides.sh

# 2. explanation.md の節をスライドに割り当てて書く（下の「構成の目安」）

# 3. ビルドして、必ず PNG に描き出して目視確認する
../../tools/build_slides.sh . --preview
```

`build_slides.sh` は `latexmk -pdfdvi`（platex + dvipdfmx）でビルドし、中間ファイルを消す。
`--preview` を付けると全ページを PNG にして、はみ出しを目で確認できる。

## ファイル構成

問題フォルダ（例: `abc128/c/`）に置くもの:

| ファイル | 内容 | git |
|---|---|---|
| `slides.tex` | スライド本体 | 追跡する |
| `latexmkrc` | latexmk 設定（platex + dvipdfmx） | 追跡する |
| `slides.pdf` | ビルド成果物 | **追跡する**（見るのに TeX 環境が要らなくなる） |
| `*.aux` `*.dvi` `*.log` 等 | 中間ファイル | `.gitignore` 済み |

## ビルド環境（この PC の実際）

- TeX は **TinyTeX**: `C:\Users\takum\AppData\Roaming\TinyTeX\bin\windows\`
  （`latexmk` `platex` `uplatex` `lualatex` が PATH にある）。**TeX Live 2024 は入っていない。**
- `abc303/b` `abc454/c` `abc462/c` などにある `build_slides.ps1` は
  `C:\texlive\2024\bin\windows\latexmk.exe` を決め打ちしている旧版。
  存在しないので警告を出して platex 直叩きにフォールバックしている（動きはする）。
  **新しい問題では `tools/build_slides.sh` を使う。**
- PDF を画像化するのは **`mutool draw`**（WSL 側）。poppler の `pdftoppm` は入っていない。

## 構成の目安（explanation.md との対応）

| # | フレーム | explanation.md の対応節 |
|---|---|---|
| 1 | タイトル | ヘッダ |
| 2 | 問題の概要（具体例を 1 つ図にする） | 1. 問題 |
| 3 | まず制約を読む（計算量の見積り） | 2. 考察の起点 |
| 4-5 | アイデア（1 枚 1 アイデア。図を主役に） | 3. 解法 |
| 6 | 擬似コードと実装の要点 `[fragile]` | 4. 擬似コード / 5. 実装の要点 |
| 7 | サンプルを手で全部追う（表） | 6. サンプルで確認 |
| 8 | 一段深い見方 / 落とし穴 | 7. |
| 9 | まとめ + 同系統の問題 | 8. 覚えておくこと |

9 枚前後が目安。多いなら 1 枚に詰め込みすぎている。

## 図は TikZ で描く

雛形は `tikz` と `arrows.meta,positioning,backgrounds,fit` を読み込み済み。
状態の色分け用に `ok`（緑）/ `ng`（赤）/ `onc`（黄）を定義してある。

よく使う型:

- **ビット列・桁の並び** → `\node[draw,minimum width=..] at (x,0) {1};` を横に並べる
- **二部グラフ（スイッチ↔電球など）** → `\node[circle,draw]` + `\draw[-]` で結ぶ
- **数直線と区間** → `\draw[->]` の上に太い線分を重ねて区間を示す（`arc127/a` の 4・5 枚目）
- **棒グラフで規模を見せる** → 高さを変えた `\fill` を並べる（`abc128/c` の 3 枚目）

TikZ を選ぶ理由: ベクタなので拡大しても崩れず、`slides.tex` の diff に図の変更が乗り、
オフラインでビルドが完結する。図だけ外部ツールで作ると再現できなくなる。

## 落とし穴（実際に踏んだもの）

- **`verbatim` だけでなく `\verb` も `[fragile]` が要る。** 付け忘れると
  `LaTeX Error: \verb illegal in argument` や `Misplaced alignment tab character &` で落ちる。
- **`columns` の中の tikzpicture に注釈ノードを置くと、段の幅をはみ出して隣の段の文字と重なる。**
  注釈は `tikzpicture` の外に `{\scriptsize ...}` で置く。
- **縦のはみ出しは無言で起きる**（エラーにならず、下端の行がフッターに潜って消える）。
  `--preview` で全ページを見るまで完成としない。
- 日本語は `pxjahyper` が要る（しおりの文字化け防止）。

## 既存の実例

- [`abc128/c/slides.tex`](../abc128/c/slides.tex) — bit 全探索。棒グラフ・ビット列・二部グラフ。
- [`arc127/a/slides.tex`](../arc127/a/slides.tex) — 数直線と区間、打ち切り 3 ケースの作図。
- [`abc462/c/slides.tex`](../abc462/c/slides.tex) — 旧構成（`build_slides.ps1` 同梱）の例。
