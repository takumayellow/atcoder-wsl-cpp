#!/usr/bin/env bash
# 手書きメモの再現 + 振り返り（thinking.tex）をビルドする（lualatex。共通スタイルは tools/tex/handmemo.sty）。
#
#   使い方:
#     tools/build_thinking.sh abc048/b            # thinking.pdf を作る
#     tools/build_thinking.sh abc048/b --preview  # 各ページを PNG にして目で確かめる
#
# 手書き風のフォント（UD デジタル教科書体・Ink Free）は Windows 標準なので、Windows 側の TinyTeX でビルドする。
set -euo pipefail

PREVIEW=0
DIR_ARG=""
for arg in "$@"; do
  case "$arg" in
    --preview) PREVIEW=1 ;;
    -*) echo "error: 不明なオプション: $arg" >&2; exit 1 ;;
    *) DIR_ARG="$arg" ;;
  esac
done

TOOLS_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$(cd -- "${DIR_ARG:-.}" 2>/dev/null && pwd)" || {
  echo "error: そのディレクトリはありません: ${DIR_ARG:-.}" >&2
  exit 1
}
cd "$TARGET_DIR"
[[ -f thinking.tex ]] || { echo "error: thinking.tex がありません: $TARGET_DIR" >&2; exit 1; }

# handmemo.sty を探せるようにする（末尾の区切りで既定の検索パスも残す）。TeX には Windows 形式で渡す
SEP=":"; STY_DIR="$TOOLS_DIR/tex"
if command -v cygpath >/dev/null 2>&1; then SEP=";"; STY_DIR="$(cygpath -m "$STY_DIR")"; fi
export TEXINPUTS="$STY_DIR$SEP"

latexmk -lualatex -interaction=nonstopmode -file-line-error thinking.tex
latexmk -c thinking.tex >/dev/null 2>&1 || true
echo "built: $TARGET_DIR/thinking.pdf"

if [[ "$PREVIEW" -eq 1 ]]; then
  OUTDIR="$TARGET_DIR/.thinking_preview"
  rm -rf "$OUTDIR"; mkdir -p "$OUTDIR"
  if command -v mutool >/dev/null 2>&1; then
    mutool draw -o "$OUTDIR/p%d.png" -r 80 thinking.pdf
  else
    to_wsl() { cygpath -w "$1" | sed -e 's|\\|/|g' -e 's|^\([A-Za-z]\):|/mnt/\L\1|'; }
    MSYS2_ARG_CONV_EXCL='*' wsl.exe mutool draw \
      -o "$(to_wsl "$OUTDIR")/p%d.png" -r 80 "$(to_wsl "$PWD/thinking.pdf")"
  fi
  echo "preview: $OUTDIR/p1.png ..."
fi
