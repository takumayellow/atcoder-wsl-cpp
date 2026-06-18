#!/bin/bash
set -e

# =============================================================================
# update_cookie.sh
#
# AtCoder の Cloudflare Turnstile により `oj login` / `acc login` の対話ログイン
# は弾かれる。回避策として、ブラウザでログイン済みの Cookie を JSON エクスポート
# し、それを online-judge-tools (oj) と atcoder-cli (acc) の両方へ流し込む。
#
# 使い方:
#   1. ブラウザ(Chrome等)で atcoder.jp にログイン
#   2. 拡張機能「EditThisCookie」等で Cookie を JSON エクスポート
#   3. リポジトリ直下に cookie.json として保存
#   4. WSL で:  ./tools/update_cookie.sh
#   5. 確認:    oj login --check https://atcoder.jp/   /   acc session
# =============================================================================

# --- リポジトリルートをスクリプト位置から自動検出（ハードコードしない） ---
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

OJ_COOKIE_DIR="$HOME/.local/share/online-judge-tools"
COOKIE_JSON="$REPO_DIR/cookie.json"
CONVERT_SCRIPT="$REPO_DIR/convert_cookie.py"

if [ ! -f "$COOKIE_JSON" ]; then
    echo "Error: cookie.json not found in $REPO_DIR"
    echo "Please export cookies from AtCoder (Chrome) as JSON (e.g. using EditThisCookie extension) and save to cookie.json"
    exit 1
fi

# --- 1. oj 用: cookie.json -> cookie.jar (LWP形式) ---
echo "Converting cookie.json to cookie.jar (for oj)..."
cd "$REPO_DIR"
python3 "$CONVERT_SCRIPT"

if [ ! -f "cookie.jar" ]; then
    echo "Error: Failed to generate cookie.jar"
    exit 1
fi

mkdir -p "$OJ_COOKIE_DIR"
mv cookie.jar "$OJ_COOKIE_DIR/cookie.jar"
chmod 600 "$OJ_COOKIE_DIR/cookie.jar"
echo "[oj]  Cookie updated: $OJ_COOKIE_DIR/cookie.jar"

# --- 2. acc 用: cookie.json -> session.json (REVEL_SESSION / REVEL_FLASH) ---
# acc は oj とは別に独自のセッション (session.json) を持つため、こちらも更新する。
# 注意: Windows 側の npm acc (/mnt/c/.../AppData/Roaming/npm/acc) が PATH 先頭に
# いると WSL bash では正しく動かない(exit 127)。nvm の Linux 版 acc を優先する。
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
elif [ -d "$HOME/.nvm/versions/node" ]; then
    LATEST_NODE=$(ls -d "$HOME"/.nvm/versions/node/v* 2>/dev/null | sort -V | tail -n 1)
    [ -n "$LATEST_NODE" ] && export PATH="$LATEST_NODE/bin:$PATH"
fi
export PATH="$HOME/.local/bin:$PATH"

# Linux(/home, /usr 配下)の acc を明示的に探す。Windows(/mnt/c)版は除外。
ACC_BIN="$(command -v acc 2>/dev/null || true)"
case "$ACC_BIN" in
    /mnt/*|"") ACC_BIN="$(ls "$HOME"/.nvm/versions/node/v*/bin/acc 2>/dev/null | sort -V | tail -n 1)";;
esac

if [ -n "$ACC_BIN" ] && [ -x "$ACC_BIN" ]; then
    ACC_CONFIG_DIR="$("$ACC_BIN" config-dir 2>/dev/null || true)"
    if [ -n "$ACC_CONFIG_DIR" ] && [ -d "$ACC_CONFIG_DIR" ]; then
        python3 - "$COOKIE_JSON" "$ACC_CONFIG_DIR/session.json" <<'PY'
import json, sys

cookie_json, session_path = sys.argv[1], sys.argv[2]
with open(cookie_json) as f:
    data = json.load(f)

# acc が必要とするのは REVEL_FLASH と REVEL_SESSION。
wanted = ("REVEL_FLASH", "REVEL_SESSION")
by_name = {c["name"]: c.get("value", "") for c in data if c.get("name") in wanted}

cookies = []
for name in wanted:
    if name in by_name:
        cookies.append(f"{name}={by_name[name]}")

if not any(c.startswith("REVEL_SESSION=") for c in cookies):
    print("[acc] WARNING: REVEL_SESSION not found in cookie.json; session.json not updated")
    sys.exit(0)

with open(session_path, "w") as f:
    json.dump({"cookies": cookies}, f, indent="\t")
print(f"[acc] Session updated: {session_path}")
PY
    else
        echo "[acc] WARNING: could not resolve acc config-dir; skipped session.json update"
    fi
else
    echo "[acc] WARNING: acc not found on PATH; skipped session.json update"
fi

echo ""
echo "Done. Verify with:"
echo "  oj login --check https://atcoder.jp/"
echo "  acc session"
echo "If it still fails, re-export cookie.json from a fresh browser session and re-run."
