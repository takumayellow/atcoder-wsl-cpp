# 手書きメモの扱い

紙に書いた考察メモ（スマホで撮影したもの）は、**原本の画像を Box に、読み解いた内容をこのリポジトリに**分けて置く。
リポジトリには撮影画像・スキャンを入れない。読み解きは `thinking.tex` に書き、
メモを**手書き風に描き直したページ**と**振り返りのページ**を 1 つの `thinking.pdf` にまとめる。
例: [abc048/b/thinking.pdf](../abc048/b/thinking.pdf)

## 置き場所

| もの | 置き場所 | git |
|------|----------|-----|
| 撮影した原本（jpg） | `Box/Photo Backup/手書き/atcoder/<contest>/<問題>/<撮影ファイル名>.jpg` | 入れない |
| 読み解き（メモの再現 + 振り返り） | `<問題フォルダ>/thinking.tex` | 入れる |
| そのビルド結果 | `<問題フォルダ>/thinking.pdf` | 入れる（`slides.pdf` と同じ。TeX 環境なしで見られるように） |
| 手書き風の共通スタイル | `tools/tex/handmemo.sty` | 入れる |
| 清書した解説 | `<問題フォルダ>/explanation.md`（従来どおり） | 入れる |
| スキャンしたメモ・図の書き出し（`memo.pdf`, `*.png` など） | `Box/Photo Backup/手書き/atcoder/<元のパス>` | 入れない |
| 外部の参考資料・配布された問題 PDF | `Box/private/repo-assets/atcoder-wsl-cpp/<元のパス>` | 入れない |

2026-09-25 に、それまで git に入っていた原本を上の置き場所へ移した（パスは元のまま）。
`abc303/b/abc303 b.pdf`、`abc462/c/memo.pdf`、`agc003/a/*.png` は手書き側、
`abc462/c/slides_notebooklm_DESIGN_REF.pdf`、`icpc/contest/2026/JAG/domestic-2026-problemset.pdf` は repo-assets 側にある。

- **問題フォルダは、その問題のコードが既にあるフォルダ**にする（`ls -d */<問題>` と `other/*/<問題>` を探す）。
  無ければ `<contest>/<問題>`（問題 ID `abc048_b` の最後の `_` で分ける）。
  例: code festival 2017 予選 C の B は `other/code-festival-2017-qualc/b/`。
- Box 側は常に `手書き/atcoder/<contest>/<問題>/`（contest は問題 ID のまま。例 `code_festival_2017_qualc/b`）。
- 撮影ファイル名は端末が付けた `YYYYMMDD_HHMMSS.jpg` のまま変えない（撮影時刻で原本を引ける）。
- どの写真をどこへ振り分けたかは `Box/Photo Backup/phone/_ledger/<取り込み日>.tsv`（元ファイル名・sha256・Box 上のパス）に残る。

## 問題の特定

メモに問題名が書いていなくても、提出履歴から絞り込める。

1. AtCoder Problems API で自分（`yellowred`）の提出を全件取る
   `https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=yellowred&from_second=<N>`
   （1 回 500 件まで。最後の `epoch_second + 1` を次の `from_second` にして繰り返す）
2. 撮影日の直前 1〜2 か月に AC した問題を題名つきで並べる
   （題名は `https://kenkoooo.com/atcoder/resources/problems.json`）
3. メモに書いた変数名・サンプル入力・題名の断片と問題文を突き合わせる
4. 提出ソースは `curl -A "Mozilla/5.0" https://atcoder.jp/contests/<c>/submissions/<id>` で取る（UA が無いと 403）。
   WA/TLE → AC の順番と差分から、どこで間違えたかを読む

## thinking.tex の構成

```bash
tools/build_thinking.sh abc048/b --preview   # thinking.pdf を作り、全ページを PNG に描き出す
```

lualatex でビルドする（`tools/tex/handmemo.sty` を読む）。フォントは Windows 標準の
UD デジタル教科書体と Ink Free なので、Windows 側の TinyTeX でビルドする。

1. **メモの再現（原本 1 枚 = 1 ページ）** — `memopage` 環境。方眼 18 × 26 cm、左上が (0,0)、下が +y。
   写真を見ながら、書いてある位置・順番のまま置く。ページの順番は撮影時刻ではなく**書いた内容の流れ**にする。
2. **振り返り（1 ページ）** — 普通の組版で、次の 3 節。図が効くなら TikZ で 1 つ入れる。
   - つまずき（どの提出がなぜ落ちたか。無ければ「無し」と書き、効いた発想を残す）
   - 正しい考え方（短く。長くなるなら explanation.md に書いてリンクする）
   - 次に活かすこと

冒頭の箇条書きに、問題 URL・提出の流れ（各提出へのリンク）・Box の原本の場所を書く。

### 色の決まり

| 色 | 意味 | マクロ |
|----|------|--------|
| 黒（インク） | 原本に書いてあること | `\hw` `\hwm` `\hwstrike` `\hwcircle` `\hwline` |
| 赤（赤ペン） | 後から見返して入れた指摘（原本に無い） | `\redpen` `\redarrow` `\redbox` |
| 灰色の点線枠 | 読めない所 | `\hwunread` |

黒と赤を混ぜない。**原本に無いことを黒で書かない。**

```latex
\begin{memopage}{20260925\_174824.jpg}
  \hw(1.4,1.3){B --- Between a and b ...}          % 手書きの文字（$...$ も混ぜてよい）
  \hwm(0.8,15.2){\floor{\frac{b}{x}} - \floor{\frac{a}{x}}}   % 手書きの数式
  \hwstrike(5.8,9.8){\ttfamily\hwlfont x \% m == 0}  % 書いて消したもの
  \hwcircle(2.3,4.2)(1.6,1.0)                        % 丸囲み（中心と半径）
  \hwunread(13.9,8.6){「4」は 9 にも見える}           % 読めない所
  \redpen(9.6,23.4){a=1 は割り切れない → WA}         % 赤ペン
  \redarrow(12.2,24.1)(10.7,25.5)
\end{memopage}
```

### 書くときの注意

- 読めない箇所は推測で埋めず `\hwunread` にする。「たぶんこう」を黒で書かない。
- 赤ペンは「そのとき何を見落としたか」に絞る。1 ページ 3〜5 個が目安。本文に重ねない。
- 提出コードの誤り・メモの誤記を書くときは、落ちる入力を実際に動かして確かめてから書く。
- ビルド後に `--preview` の PNG を全部見て、はみ出し・重なりを確かめる（エラーにならずに重なる）。
