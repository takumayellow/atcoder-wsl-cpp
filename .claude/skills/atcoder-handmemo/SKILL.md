---
name: atcoder-handmemo
description: 紙に書いた AtCoder の考察メモ（Box の撮影画像）から問題を特定し、メモを手書き風に描き直した thinking.tex → thinking.pdf と、振り返りの thinking.md にする。「手書きメモを起こして」「このメモの問題どれ？」「メモを tex にして」「thinking 作って」等で使う
---

# atcoder-handmemo

撮影した考察メモ 1 問ぶんを、`<問題フォルダ>/thinking.tex`（→ `thinking.pdf`。メモの再現）と `thinking.md`（振り返りの文章）にする。
同じ文章を両方に書かない。手書きの PDF・スキャンは写真と同じく Box に置き、リポジトリに入れない。
置き場所・色の決まり・マクロの正本は [`docs/handwritten-memos.md`](../../../docs/handwritten-memos.md)。**最初にそれを読む。**
完成形の例は `abc048/b/thinking.tex` と `thinking.md`。迷ったらこれを写して直す。

写真をスマホから Box へ取り込む所までは、このスキルの範囲外（dotfiles の `photo-intake` スキル）。
ここは Box の `Photo Backup/手書き/atcoder/<contest>/<問題>/` に原本がある状態から始める。

## 手順

1. **原本を見る**
   - `ls "$HOME/Box/Photo Backup/手書き/atcoder/<contest>/<問題>/"`。
   - Read で見るときは、EXIF の向きを直して長辺 1600px に縮めた複製を scratchpad に作ってから見る（Pillow の `ImageOps.exif_transpose`）。
   - 上下逆・横向きの写真もある。
   - 原本はリポジトリにコピーしない（`.gitignore` 済みだが、そもそも置かない）。
2. **問題を特定する**（フォルダが未定のとき）
   - docs の「問題の特定」の順に、kenkoooo の提出一覧 × 撮影日 × メモの断片で絞る。
   - 提出ソースを取り、TLE/WA → AC の差分を読む。
3. **問題フォルダを決める**
   - コードが既にあるフォルダを使う（`other/` の下も探す）。
   - 同じフォルダに古い `thinking.md` があれば、下の形に書き直す（読み解きの事実は落とさない）。
4. **thinking.tex を書く**
   - 原本 1 枚につき `memopage` を 1 つ作る。
     - 写真上の位置を 18 × 26 cm に比例で写す。
     - 書いた順・消した線・丸囲みまで原本どおりに置く。
     - 読めない所は `\hwunread`。
   - 赤ペン（`\redpen` / `\redarrow` / `\redbox`）は、後から見返した指摘だけにする。
     - 例：どの提出で何が起きたか、どの検算が偏っていたか。
     - 原本に無いことを黒で書かない。
   - 図が効くなら、最後に TikZ の図を 1 ページだけ置く（文章は md へ）。
5. **thinking.md を書く**
   - 冒頭に問題 URL・提出の流れ（リンク）・Box の場所・`thinking.pdf` へのリンク。
   - `## つまずき` / `## 正しい考え方` / `## 次に活かすこと`。数式は GitHub の `$...$`。
6. **確かめる**
   - 「AC したコードに残るバグ」「メモの誤記」を書くなら、落ちる入力を実際に動かして確かめる。
     - C++ は WSL 経由でビルドする（`atcoder-explain` コマンドの 3. と同じ）。
   - `tools/build_thinking.sh <問題フォルダ> --preview` を実行し、`.thinking_preview/p*.png` を**全部** Read で見る。
     - はみ出しや重なりはエラーにならないので、目で探す。
     - 原本の写真と並べ、書き漏れ・位置のずれを直す。
7. **終える**
   - `thinking.tex`・`thinking.pdf`・`thinking.md` をコミットする。
   - PR を作るところまでで、**マージはしない**。
   - ユーザーに PDF を開いて見せる（`cmd //c start "" <pdf の Windows パス>`）。

## ハマりどころ

- フォントは `C:/Windows/Fonts/` のファイルを直接指している。名前指定だと luaotfload が見つけられない。
- `handmemo.sty` を sed で書き換えない。置換文字列の `\u` が「次を大文字に」と解釈されて `\usetikzlibrary` が壊れた。
- `memopage` の中の数式は、手書き書体（mathastext の `hand` 版）になる。振り返りのページは普段の数式に戻る。
- `\verb` はノードの中で使えない。コードは `{\ttfamily\hwlfont ...}` で書く。
