#!/bin/bash
set -e

# WSL Path to repo
REPO_DIR="/mnt/c/Users/takum/Documents/atcoder/atcoder-wsl-cpp"
OJ_COOKIE_DIR="$HOME/.local/share/online-judge-tools"
COOKIE_JSON="$REPO_DIR/cookie.json"
CONVERT_SCRIPT="$REPO_DIR/convert_cookie.py"

if [ ! -f "$COOKIE_JSON" ]; then
    echo "Error: cookie.json not found in $REPO_DIR"
    echo "Please export cookies from AtCoder (Chrome) as JSON (e.g. using EditThisCookie extension) and save to cookie.json"
    exit 1
fi

echo "Converting cookie.json to cookie.jar..."
cd "$REPO_DIR"
python3 "$CONVERT_SCRIPT"

if [ ! -f "cookie.jar" ]; then
    echo "Error: Failed to generate cookie.jar"
    exit 1
fi

mkdir -p "$OJ_COOKIE_DIR"
mv cookie.jar "$OJ_COOKIE_DIR/cookie.jar"
chmod 600 "$OJ_COOKIE_DIR/cookie.jar"

echo "Success: Cookie updated in $OJ_COOKIE_DIR/cookie.jar"
echo "You can now try submitting with 'acsub' again."
echo "If it still fails, please re-export cookie.json from a fresh browser session."
