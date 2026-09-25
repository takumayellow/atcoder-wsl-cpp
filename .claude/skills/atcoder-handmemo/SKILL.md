---
name: atcoder-handmemo
description: 紙に書いた AtCoder の考察メモ（Box の撮影画像）から問題を特定し、メモを手書き風に描き直したページと振り返りを thinking.tex → thinking.pdf にまとめる。「手書きメモを起こして」「このメモの問題どれ？」「メモを tex にして」等で使う
---

# atcoder-handmemo

撮影した考察メモ 1 問ぶんを、`<問題フォルダ>/thinking.tex` → `thinking.pdf` にする。
PDF は「メモの再現（原本 1 枚 = 1 ページ）」と「振り返り（1 ページ）」の 2 部で、**PDF 1 つを見れば一通り分かる**ようにする。md は作らない。
手書きの PDF・スキャンは写真と同じく Box に置き、リポジトリに入れない。
置き場所・色の決まり・問題の特定方法の正本は [`docs/handwritten-memos.md`](../../../docs/handwritten-memos.md)。**最初にそれを読む。**
完成形の例は `abc048/b/thinking.tex`。迷ったらこれを写して直す。

写真をスマホから Box へ取り込む所までは、このスキルの範囲外（dotfiles の `photo-intake` スキル）。
ここは Box の `Photo Backup/手書き/atcoder/<contest>/<問題>/` に原本がある状態から始める。

## 描き直しに使う道具（`tools/tex/handmemo.sty`）

`thinking.tex` は `\usepackage{handmemo}` で読む自作のスタイルで描く。中身は TikZ（LaTeX の作図パッケージ）の薄い包みで、
使うのは次のマクロだけ。定義と引数の説明は sty の冒頭とそれぞれの直前のコメントにある。

| マクロ | 意味 |
|--------|------|
| `\begin{memopage}{<原本ファイル名>}` … `\end{memopage}` | 原本 1 枚ぶんの方眼紙（18 × 26 cm、左上が (0,0)、下が +y）。引数は右上に出る原本名 |
| `\hw(x,y){文字}` / `\hwm(x,y){数式}` | 手書きの文字 / 数式（左端を (x,y) に置く） |
| `\hwstrike` `\hwcircle` `\hwline` `\hwbag` | 書いて消したもの・丸囲み・手で引いた線・上が開いた U 字 |
| `\hwunread(x,y){補足}` / `\hwunreadmark(x,y)` | 読めない所（補足つきの枠 / 行の中の 1〜2 字用の「?」枠） |
| `\redpen` `\redarrow` `\redbox` | 後から見返して入れる赤ペン（文字・矢印・囲み） |

この表に無い形が要るときは、その tex の中で `\draw` を直接書く。2 問以上で使いそうなら sty に足す。

## 手順

1. **原本を見る**
   - `ls "$HOME/Box/Photo Backup/手書き/atcoder/<contest>/<問題>/"`。
   - Read で見るときは、EXIF の向きを直して長辺 1600px に縮めた複製を scratchpad に作ってから見る（Pillow の `ImageOps.exif_transpose`）。
   - 上下逆・横向きの写真もある。
   - 原本はリポジトリにコピーしない（`.gitignore` 済みだが、そもそも置かない）。
2. **問題を特定する**（フォルダが未定のとき）
   - AtCoder Problems（kenkoooo.com）の API で自分（`yellowred`）の提出一覧を取り、撮影日の前 1〜2 か月に AC した問題を、メモの断片（変数名・サンプル入力）と突き合わせて絞る。
     URL と手順は docs の「問題の特定」にある。
   - 提出ソースを取り、TLE/WA → AC の差分を読む。
3. **問題フォルダを決める**
   - コードが既にあるフォルダを使う（`other/` の下も探す）。
   - 同じフォルダに古い `thinking.md` があれば、中身を tex に移して md は消す。
4. **thinking.tex を書く**
   - 原本 1 枚につき `memopage` を 1 つ作る。
     - 写真上の位置を 18 × 26 cm に比例で写す。
     - 書いた順・消した線・丸囲みまで原本どおりに置く。
     - 読めない所は `\hwunread` / `\hwunreadmark`。
   - 赤ペン（`\redpen` / `\redarrow` / `\redbox`）は、後から見返した指摘だけにする。
     - 例：どの提出で何が起きたか、どの検算が偏っていたか。
     - 原本に無いことを黒で書かない。
   - 最後の振り返りページ：冒頭に問題 URL・提出の流れ（リンク）・Box の場所。
     その下に「つまずき / 正しい考え方 / 次に活かすこと」。図が効くなら「正しい考え方」に TikZ で 1 つ入れる。
5. **確かめる**
   - 「AC したコードに残るバグ」「メモの誤記」を書くなら、落ちる入力を実際に動かして確かめる。
     - C++ は WSL 経由でビルドする（`atcoder-explain` コマンドの 3. と同じ）。
   - `tools/build_thinking.sh <問題フォルダ> --preview` を実行し、`.thinking_preview/p*.png` を**全部** Read で見る。
     - はみ出しや重なりはエラーにならないので、目で探す。
     - 原本の写真と並べ、書き漏れ・位置のずれを直す。
6. **終える**
   - `thinking.tex` と `thinking.pdf` をコミットする。
   - PR を作るところまでで、**マージはしない**。
   - ユーザーに PDF を開いて見せる（`cmd //c start "" <pdf の Windows パス>`）。

## ハマりどころ

- フォントは `C:/Windows/Fonts/` のファイルを直接指している。名前指定だと luaotfload が見つけられない。
- `handmemo.sty` を sed で書き換えない。GNU sed は置換文字列の中の `\u` を「次の 1 字を大文字に」と解釈するので、
  `\usetikzlibrary` を含む行を sed の置換で書き直すと壊れる。Edit で直す。
- `memopage` の中の数式は、手書き書体（mathastext の `hand` 版）になる。振り返りのページは普段の数式に戻る。
- `\verb` はノードの中で使えない。コードは `{\ttfamily\hwlfont ...}` で書く。
- `\redbox` などで「Dimension too large」が出たら、座標を少しずらす。直した後も latexmk が前回の失敗を覚えていて通らないときは `thinking.fdb_latexmk` を消す。
