# 手書きメモの扱い

紙に書いた考察メモ（スマホで撮影したもの）は、**原本の画像を Box に、読み解いた内容をこのリポジトリに**分けて置く。
リポジトリには画像・PDF などのバイナリを入れない。

## 置き場所

| もの | 置き場所 | git |
|------|----------|-----|
| 撮影した原本（jpg） | `Box/Photo Backup/手書き/atcoder/<contest>/<問題>/<撮影ファイル名>.jpg` | 入れない |
| 読み解き（思考の再構成） | `<contest>/<問題>/thinking.md` | 入れる |
| 清書した解説 | `<contest>/<問題>/explanation.md`（従来どおり） | 入れる |
| スキャンしたメモ・図の書き出し（`memo.pdf`, `*.png` など） | `Box/Photo Backup/手書き/atcoder/<元のパス>` | 入れない |
| 外部の参考資料・配布された問題 PDF | `Box/private/repo-assets/atcoder-wsl-cpp/<元のパス>` | 入れない |

`slides.pdf` など tex から作る成果物の扱いは [tools/slides_guide.md](../tools/slides_guide.md) に従う（ここでは変えない）。

2026-09-25 に、それまで git に入っていた原本を上の置き場所へ移した（パスは元のまま）。
`abc303/b/abc303 b.pdf`、`abc462/c/memo.pdf`、`agc003/a/*.png` は手書き側、
`abc462/c/slides_notebooklm_DESIGN_REF.pdf`、`icpc/contest/2026/JAG/domestic-2026-problemset.pdf` は repo-assets 側にある。

- `<contest>` / `<問題>` はコード用ディレクトリと同じ（例: `abc048/b`, `code_festival_2017_qualc/b`）。
  問題 ID `abc048_b` の最後の `_` で分ける。
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

## thinking.md の書き方

`explanation.md` が「正しい解き方の清書」なのに対し、`thinking.md` は**そのとき自分がどう考え、どこで間違えたか**の記録。
メモと提出履歴（WA/TLE の順番）から再構成する。

```markdown
# <contest> <問題> - <題名>

- 問題: <URL>
- 手書き原本: `Box/Photo Backup/手書き/atcoder/<contest>/<問題>/`（<ファイル名>、撮影 YYYY-MM-DD）
- 提出: <日付> <言語> TLE → WA → AC（各提出の URL）

## メモで考えたこと
<メモに書いてある順に、何を置き、何を試したか>

## つまずき
<どこで誤解したか・どの提出がなぜ落ちたか。無ければ「無し」と書き、効いた発想を残す>

## 正しい考え方
<短く。長くなるなら explanation.md に書いてリンクする>

## 次に活かすこと
<次に同じ型の問題に当たったときにやること>
```

- メモにない推測を事実のように書かない。読めない箇所は「判読不能」と書く。
- 提出コードの誤りは、落ちる入力を実際に動かして確かめてから書く。
