#!/usr/bin/env bash
# 解説スライド slides.tex + latexmkrc の雛形を問題フォルダに作る。
#
#   使い方:
#     cd abc128/c && ../../tools/new_slides.sh
#     tools/new_slides.sh abc128/c        # パス指定でも可
#
# 先に explanation.md を書いてから使う（スライドは Markdown 正本の再構成であって、
# 別々に考察を書くものではない）。タイトルは contest.acc.json から自動で埋める。
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$REPO_ROOT/tools/templates/slides.tex"
LATEXMKRC_TEMPLATE="$REPO_ROOT/tools/templates/latexmkrc"

TARGET_DIR="$(cd -- "${1:-.}" 2>/dev/null && pwd)" || {
  echo "error: そのディレクトリはありません: ${1:-.}" >&2
  exit 1
}
OUT="$TARGET_DIR/slides.tex"

for f in "$TEMPLATE" "$LATEXMKRC_TEMPLATE"; do
  if [[ ! -f "$f" ]]; then
    echo "error: テンプレートが見つかりません: $f" >&2
    exit 1
  fi
done
if [[ -e "$OUT" ]]; then
  echo "error: すでに存在します（上書きしません）: $OUT" >&2
  exit 1
fi

PROBLEM="$(basename "$TARGET_DIR")"                 # 例: c
CONTEST="$(basename "$(dirname "$TARGET_DIR")")"    # 例: abc128

if [[ ! "$PROBLEM" =~ ^[a-z]{1,2}$ ]]; then
  echo "error: 問題フォルダ（a/b/c/... または ex）の中で実行してください: $TARGET_DIR" >&2
  exit 1
fi

# タイトルは .tex に直接埋まるので、LaTeX の特殊文字を潰す
# （"A & B" や "n_i" のようなタイトルでビルドが落ちるのを防ぐ）。\ を最初に処理する。
# 改行は sed の置換を壊すので落とす。
latex_esc() {
  printf '%s' "$1" | tr -d '\r\n' | sed \
    -e 's|\\|\\textbackslash{}|g' \
    -e 's|[&%$#_{}]|\\&|g' \
    -e 's|~|\\textasciitilde{}|g' \
    -e 's|\^|\\textasciicircum{}|g'
}

TITLE="{{TITLE}}"   # 見つからなければプレースホルダのまま残す（手で埋める）

# 動く python を探す。Git Bash の `python3` は Microsoft Store のスタブのことがあり、
# command -v は通るのに実行すると失敗する（＝タイトル補完が黙って効かない）。
PY=""
for _cand in python3 python; do
  if command -v "$_cand" >/dev/null 2>&1 && "$_cand" -c 'pass' >/dev/null 2>&1; then
    PY="$_cand"
    break
  fi
done

# contest.acc.json があれば問題タイトルを引く
ACC_JSON="$(dirname "$TARGET_DIR")/contest.acc.json"
if [[ -f "$ACC_JSON" && -n "$PY" ]]; then
  read -r -d '' _py <<'PYEOF' || true
import json, sys
path, label = sys.argv[1], sys.argv[2].upper()
try:
    d = json.load(open(path, encoding="utf-8"))
except Exception:
    sys.exit(0)
for t in d.get("tasks", []):
    if t.get("label", "").upper() == label:
        print(t.get("title", ""))
        break
PYEOF
  _t="$("$PY" -c "$_py" "$ACC_JSON" "$PROBLEM" 2>/dev/null || true)"
  [[ -n "$_t" ]] && TITLE="$(latex_esc "$_t")"
fi

# sed の置換文字列側で特殊になる | & \ を潰す
esc() { printf '%s' "$1" | sed -e 's|[|&\\]|\\&|g'; }

sed \
  -e "s|{{CONTEST_UPPER}}|$(esc "$(echo "$CONTEST" | tr '[:lower:]' '[:upper:]')")|g" \
  -e "s|{{PROBLEM_UPPER}}|$(esc "$(echo "$PROBLEM" | tr '[:lower:]' '[:upper:]')")|g" \
  -e "s|{{TITLE}}|$(esc "$TITLE")|g" \
  -e "s|{{CONTEST}}|$(esc "$CONTEST")|g" \
  "$TEMPLATE" > "$OUT"

if [[ ! -e "$TARGET_DIR/latexmkrc" ]]; then
  cp "$LATEXMKRC_TEMPLATE" "$TARGET_DIR/latexmkrc"
  echo "created: $TARGET_DIR/latexmkrc"
fi

echo "created: $OUT"
echo "  ビルド: $REPO_ROOT/tools/build_slides.sh $TARGET_DIR"
