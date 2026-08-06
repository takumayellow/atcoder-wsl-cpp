#!/usr/bin/env bash
# 解説資料 explanation.md の雛形を問題フォルダに作る。
#
#   使い方:
#     cd abc128/c && ../../tools/new_explanation.sh
#     tools/new_explanation.sh abc128/c        # パス指定でも可
#
# コンテスト名 / 問題タイトル / URL は、acc が生成する contest.acc.json から
# 自動で埋める（無ければプレースホルダのまま残すので手で書く）。
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATE="$REPO_ROOT/tools/templates/explanation.md"

# cd -- で、- 始まりの引数がオプション扱いされるのを防ぐ。
# 存在しないパスは set -e 任せにせず、ここで理由の分かるエラーにする。
TARGET_DIR="$(cd -- "${1:-.}" 2>/dev/null && pwd)" || {
  echo "error: そのディレクトリはありません: ${1:-.}" >&2
  exit 1
}
OUT="$TARGET_DIR/explanation.md"

if [[ ! -f "$TEMPLATE" ]]; then
  echo "error: テンプレートが見つかりません: $TEMPLATE" >&2
  exit 1
fi
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

PROBLEM_URL="https://atcoder.jp/contests/$CONTEST/tasks/${CONTEST}_${PROBLEM}"
EDITORIAL_URL="https://atcoder.jp/contests/$CONTEST/editorial"
CONTEST_FULL_NAME="{{CONTEST_FULL_NAME}}"
TITLE="{{TITLE}}"

# contest.acc.json があればコンテスト名と問題タイトルを引く
ACC_JSON="$(dirname "$TARGET_DIR")/contest.acc.json"
if [[ -f "$ACC_JSON" ]] && command -v python3 >/dev/null 2>&1; then
  read -r -d '' _py <<'PYEOF' || true
import json, sys
path, label = sys.argv[1], sys.argv[2].upper()
try:
    d = json.load(open(path, encoding="utf-8"))
except Exception:
    sys.exit(0)
print(d.get("contest", {}).get("title", ""))
for t in d.get("tasks", []):
    if t.get("label", "").upper() == label:
        print(t.get("title", ""))
        print(t.get("url", ""))
        break
PYEOF
  mapfile -t _info < <(python3 -c "$_py" "$ACC_JSON" "$PROBLEM")
  [[ -n "${_info[0]:-}" ]] && CONTEST_FULL_NAME="${_info[0]}"
  [[ -n "${_info[1]:-}" ]] && TITLE="${_info[1]}"
  [[ -n "${_info[2]:-}" ]] && PROBLEM_URL="${_info[2]}"
fi

# sed の区切りに / は使えない（URL に含まれる）ので | を使う。
# 置換文字列側の | と & は sed の特殊文字なのでエスケープする
# （問題タイトルに "A & B" のような文字が来ても壊れないように）。
esc() { printf '%s' "$1" | sed -e 's|[|&\\]|\\&|g'; }

sed \
  -e "s|{{CONTEST_UPPER}}|$(esc "$(echo "$CONTEST" | tr '[:lower:]' '[:upper:]')")|g" \
  -e "s|{{PROBLEM_UPPER}}|$(esc "$(echo "$PROBLEM" | tr '[:lower:]' '[:upper:]')")|g" \
  -e "s|{{CONTEST_FULL_NAME}}|$(esc "$CONTEST_FULL_NAME")|g" \
  -e "s|{{TITLE}}|$(esc "$TITLE")|g" \
  -e "s|{{PROBLEM_URL}}|$(esc "$PROBLEM_URL")|g" \
  -e "s|{{EDITORIAL_URL}}|$(esc "$EDITORIAL_URL")|g" \
  -e "s|{{CONTEST}}|$(esc "$CONTEST")|g" \
  -e "s|{{PROBLEM}}|$(esc "$PROBLEM")|g" \
  "$TEMPLATE" > "$OUT"

echo "created: $OUT"
echo "  未確定のプレースホルダ（{{POINTS}} / {{DATE}} など）は問題ページを見て埋めること。"
