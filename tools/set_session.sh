#!/usr/bin/env bash
# Refresh the AtCoder session from a REVEL_SESSION value pasted at the prompt.
#
# The EditThisCookie export in the README is the full-fidelity path, but oj and
# acc only need REVEL_SESSION. This asks for that one value with the terminal
# echo off, writes cookie.json in the shape convert_cookie.py expects, and then
# hands off to update_cookie.sh, so the token never lands in shell history or in
# a terminal scrollback.
#
# Where to find it: browser DevTools > Application > Cookies > https://atcoder.jp
# > REVEL_SESSION > copy the Value column.
#
#   ./tools/set_session.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

printf 'Paste REVEL_SESSION (input hidden), then Enter: ' >&2
read -rs REVEL_SESSION
printf '\n' >&2

if [ -z "${REVEL_SESSION}" ]; then
    echo "Error: empty value; nothing written." >&2
    exit 1
fi

# A year out. AtCoder rotates the session itself, so this only has to outlive
# the browser cookie it was copied from.
EXPIRES=$(( $(date +%s) + 60 * 60 * 24 * 365 ))

REVEL_SESSION="$REVEL_SESSION" EXPIRES="$EXPIRES" python3 - "$REPO_DIR/cookie.json" <<'PY'
import json
import os
import sys

path = sys.argv[1]
cookie = {
    "name": "REVEL_SESSION",
    "value": os.environ["REVEL_SESSION"].strip(),
    "domain": "atcoder.jp",
    "path": "/",
    "secure": True,
    "httpOnly": True,
    "expirationDate": float(os.environ["EXPIRES"]),
}
with open(path, "w", encoding="utf-8") as f:
    json.dump([cookie], f, indent=2)
PY

chmod 600 "$REPO_DIR/cookie.json"
echo "cookie.json rewritten with the pasted REVEL_SESSION."

"$SCRIPT_DIR/update_cookie.sh"

echo
echo "Verifying..."
oj login --check https://atcoder.jp/ 2>&1 | tail -2
acc session 2>&1 | tail -2
