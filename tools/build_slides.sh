#!/usr/bin/env bash
# 解説スライドをビルドする（latexmk -pdfdvi = platex + dvipdfmx）。
#
#   使い方:
#     cd abc128/c && ../../tools/build_slides.sh
#     cd abc128/c && ../../tools/build_slides.sh --preview   # パス省略 + preview
#     tools/build_slides.sh abc128/c --preview   # 各ページを PNG に描き出して目視確認する
#
# 各問題フォルダの build_slides.ps1 は latexmk のパスを C:\texlive\2024 に決め打ちしている
# 旧版（この PC の TeX は TinyTeX で、そこには無い）。新しい問題ではこちらを使う。
set -euo pipefail

# オプションと位置引数は順序を問わない（フォルダ内から --preview だけ渡せるように）
PREVIEW=0
DIR_ARG=""
for arg in "$@"; do
  case "$arg" in
    --preview) PREVIEW=1 ;;
    -*) echo "error: 不明なオプション: $arg" >&2; exit 1 ;;
    *)
      if [[ -n "$DIR_ARG" ]]; then
        echo "error: ディレクトリは 1 つだけ指定できます: $DIR_ARG / $arg" >&2
        exit 1
      fi
      DIR_ARG="$arg"
      ;;
  esac
done

TARGET_DIR="$(cd -- "${DIR_ARG:-.}" 2>/dev/null && pwd)" || {
  echo "error: そのディレクトリはありません: ${DIR_ARG:-.}" >&2
  exit 1
}

cd "$TARGET_DIR"

if [[ ! -f slides.tex ]]; then
  echo "error: slides.tex がありません: $TARGET_DIR（tools/new_slides.sh で作る）" >&2
  exit 1
fi
if ! command -v latexmk >/dev/null 2>&1; then
  echo "error: latexmk が PATH にありません。TinyTeX の bin を PATH に通すこと:" >&2
  echo "       C:\\Users\\takum\\AppData\\Roaming\\TinyTeX\\bin\\windows" >&2
  exit 1
fi

latexmk -pdfdvi slides.tex
latexmk -c slides.tex >/dev/null 2>&1 || true
echo "built: $TARGET_DIR/slides.pdf"

if [[ "$PREVIEW" -eq 1 ]]; then
  # PDF を目で見ないと、はみ出し・図の衝突は検出できない。
  # poppler (pdftoppm) は入っていないので mutool を使う（WSL 側にある）。
  # 出力先は毎回同じ .slides_preview/（毎回作り直す。temp が溜まらず、パスが安定して開きやすい）。
  OUTDIR="$TARGET_DIR/.slides_preview"
  rm -rf "$OUTDIR"
  mkdir -p "$OUTDIR"
  if command -v mutool >/dev/null 2>&1; then
    mutool draw -o "$OUTDIR/p%d.png" -r 90 slides.pdf
  else
    # Git Bash から WSL の mutool を呼ぶ。MSYS と WSL でパスの見え方が違うので、
    # Windows パス（cygpath -w）を経由して /mnt/c/... に直してから渡す。
    to_wsl() { cygpath -w "$1" | sed -e 's|\\|/|g' -e 's|^\([A-Za-z]\):|/mnt/\L\1|'; }
    MSYS2_ARG_CONV_EXCL='*' wsl.exe mutool draw \
      -o "$(to_wsl "$OUTDIR")/p%d.png" -r 90 "$(to_wsl "$PWD/slides.pdf")"
  fi
  echo "preview: $OUTDIR/p1.png ..."
fi
