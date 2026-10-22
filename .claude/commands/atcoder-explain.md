---
description: 解いた AtCoder 問題の解説資料 (explanation.md) を作り、コードに詳細コメントを追記し、必要なら Beamer スライドも作る
argument-hint: "[問題フォルダ (例: abc128/c)。省略時は直近に触った問題フォルダ] [--slides]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

対象: $ARGUMENTS （空なら、直近に編集された問題フォルダを `ls -t` 等で特定して確認を取る）

このリポジトリの解説資料フォーマットは `tools/explanation_guide.md` に定義されている。
**まずそれを読んでから**、以下を順に実行する。

## 手順

### 1. コードを読む
- 対象フォルダの `main.cpp` / `main.py` を読み、アルゴリズムと計算量を特定する。
- 既に `explanation.md` があれば読んで、上書きではなく更新にする。

### 2. 問題情報を取得（推測で書かない）
- `WebFetch https://atcoder.jp/contests/<contest>/tasks/<contest>_<problem>`
  → タイトル・配点・制約・入力形式・全サンプル入出力
- `WebFetch https://atcoder.jp/contests/<contest>` → コンテスト正式名・開催日
- `WebFetch https://atcoder.jp/contests/<contest>/editorial` → エディトリアル URL（公式が無ければ
  ユーザー解説の URL と著者名。「公式解説」と書けるのは実在を確認できたときだけ）

### 3. サンプルで検証（PROVE-BEFORE-CLOSE）
Git Bash に `g++` は無い。**必ず WSL 経由**で実行する:

```bash
MSYS2_ARG_CONV_EXCL='*' wsl.exe bash -c 'cd /mnt/c/.../<contest>/<problem> && \
  g++ -std=gnu++17 -O2 -Wall -o /tmp/<contest><problem> main.cpp && \
  printf "<sample1>" | /tmp/<contest><problem>'
```

- **全サンプルの実出力を確認する。** 一致しなければ、そこで止めてユーザーに報告する
  （通っていないコードの解説を書かない）。
- 出力はそのまま資料の「実行ログ（検証済み）」に貼る。

### 4. explanation.md を書く
- 雛形: `tools/new_explanation.sh <dir>` で作る（既存があれば上書きせずエラーになる）。
- 節構成と禁止事項は `tools/explanation_guide.md` に従う。特に:
  - 問題文は**自分の言葉で要約**（丸ごとコピペしない）
  - **コード全文を貼らない**（要点数行の抜粋のみ）
  - サンプルを**手で追った表**を最低 1 つ置く
  - 「覚えておくこと」と**同系統の問題**を必ず書く
  - 訂正の痕跡（「〜と書きがちだが誤り」）を残さない。誤りは消して書き直す

### 5. main.cpp にコメントを追記
- **ロジックは変更しない**（コメント追記とファイル冒頭の要約ヘッダのみ）。
- 冒頭に「問題名 / URL / 解法名 / 計算量 / explanation.md 参照」の 5 行ヘッダ。
- 変数の意味、間違えやすい行（0-indexed 変換、ビット演算、ループ範囲）に行コメント。
- **追記後に再度ビルド＋全サンプル実行**して、壊していないことを確認する。

### 6. スライド（`--slides` 指定時、または図が要ると判断したとき）
フォーマットは `tools/slides_guide.md` に定義されている。**まずそれを読む**。

```bash
tools/new_slides.sh <dir>                 # slides.tex + latexmkrc の雛形
tools/build_slides.sh <dir> --preview     # ビルド + 全ページを PNG 化
```

- **explanation.md の再構成であって、考察を書き直すものではない。** 節の対応表はガイド参照。
- 図は **TikZ** で描く（ベクタ・diff が効く・オフラインで完結）。外部ツールで作った画像を
  貼らない。NotebookLM 等は音声要約やマインドマップ向けで、スライドの作図には使わない。
- `verbatim` **と `\verb`** を使うフレームには `[fragile]` が要る。
- **`--preview` で描き出した PNG を全ページ目で見るまで完成にしない。**
  縦のはみ出しはエラーにならず、下端がフッターに潜って消える。
- `slides.pdf` もコミットする（見るのに TeX 環境が要らなくなる）。

### 7. コミット
```
docs(<contest>-<problem>): 解説資料を追加 + main.cpp に注釈
```
`git add` は触ったファイルだけを明示指定する（`-A` / `.` は使わない）。
スライドを作った場合は `slides.tex` `latexmkrc` `slides.pdf` を別コミットにしてよい。

## 出力
最後に、書いた解法の要点を 5 行以内でユーザーに要約して伝える（資料の丸写しはしない）。
