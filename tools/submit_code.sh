#!/usr/bin/env bash
set -e

# --- PATH SETUP START ---
export PATH="$HOME/.local/bin:$PATH"

if ! command -v acc &> /dev/null; then
    export NVM_DIR="$HOME/.nvm"
    if [ -s "$NVM_DIR/nvm.sh" ]; then
        . "$NVM_DIR/nvm.sh"
    elif [ -d "$HOME/.nvm/versions/node" ]; then
        LATEST_NODE=$(ls -d $HOME/.nvm/versions/node/v* | sort -V | tail -n 1)
        if [ -n "$LATEST_NODE" ]; then
            export PATH="$LATEST_NODE/bin:$PATH"
        fi
    fi
fi
# --- PATH SETUP END ---

# Detect repo root for fallback lookup
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(dirname "$SCRIPT_DIR")
LAST_FILE="$HOME/.config/acx/last"

if [ ! -f "main.cpp" ] && [ ! -f "main.py" ]; then
    # If running from repo root, jump to last contest's most recent problem dir
    if [ -f "$LAST_FILE" ]; then
        LAST_CONTEST=$(cat "$LAST_FILE")
        CONTEST_DIR="$REPO_ROOT/$LAST_CONTEST"
        if [ -d "$CONTEST_DIR" ]; then
            TARGET_DIR=$(find "$CONTEST_DIR" -maxdepth 2 -type f \( -name "main.cpp" -o -name "main.py" \) -printf "%T@ %h\n" 2>/dev/null | sort -nr | head -n 1 | awk '{print $2}')
            if [ -n "$TARGET_DIR" ]; then
                cd "$TARGET_DIR"
            fi
        fi
    fi
fi

FILE=""
if [ -f "main.cpp" ]; then
    FILE="main.cpp"
elif [ -f "main.py" ]; then
    FILE="main.py"
else
    echo "Error: No main.cpp or main.py found. cd into a problem directory first."
    exit 1
fi

# Guard against known oj submit parse bugs in old versions
OJ_VER=$(oj --version 2>/dev/null | awk '{print $2}')
MIN_OJ_VER="11.5.2"
if [ -n "$OJ_VER" ]; then
    if [ "$(printf '%s\n' "$MIN_OJ_VER" "$OJ_VER" | sort -V | head -n 1)" != "$MIN_OJ_VER" ]; then
        echo "Error: online-judge-tools $OJ_VER is too old. Please update:"
        echo "  python3 -m pip install --user -U online-judge-tools online-judge-api-client"
        echo "  # If pip says already satisfied, install from GitHub:"
        echo "  python3 -m pip install --user -U git+https://github.com/online-judge-tools/online-judge-tools"
        echo "  python3 -m pip install --user -U git+https://github.com/online-judge-tools/online-judge-api-client"
        exit 1
    fi
fi

if [ "$FILE" = "main.cpp" ]; then
    LANG_CPP_ID="${OJSUB_LANG_ID_CPP:-6017}"
    :
else
    LANG_PY_ID="${OJSUB_LANG_ID_PY:-6082}"
    :
fi

# Try to resolve URL from contest.acc.json to avoid missing download history
CONTEST_JSON=""
CUR_DIR="$(pwd)"
while [ "$CUR_DIR" != "/" ]; do
    if [ -f "$CUR_DIR/contest.acc.json" ]; then
        CONTEST_JSON="$CUR_DIR/contest.acc.json"
        break
    fi
    CUR_DIR="$(dirname "$CUR_DIR")"
done

TASK_URL=""
if [ -n "$CONTEST_JSON" ]; then
    TASK_URL=$(python3 - "$CONTEST_JSON" "$(basename "$(pwd)")" <<'PY'
import json
import sys
from pathlib import Path

json_path = Path(sys.argv[1])
cur_dir = sys.argv[2].lower()
data = json.loads(json_path.read_text())
tasks = data.get("tasks", [])

def match_task(t):
    d = t.get("directory", {})
    p = (d.get("path") or "").lower()
    if p and p == cur_dir:
        return True
    label = (t.get("label") or "").lower()
    return label == cur_dir

for t in tasks:
    if match_task(t):
        url = t.get("url")
        if url:
            print(url)
            sys.exit(0)
print("")
PY
)
fi

if [ -z "$TASK_URL" ]; then
    echo "Error: failed to guess the URL to submit. Please run in a problem directory created by acc new."
    exit 1
fi

set +e
if [ "$FILE" = "main.cpp" ]; then
    oj submit -y --no-guess --language "$LANG_CPP_ID" "$TASK_URL" "$FILE" "$@"
    OJ_STATUS=$?
else
    oj submit -y --no-guess --language "$LANG_PY_ID" "$TASK_URL" "$FILE" "$@"
    OJ_STATUS=$?
fi
set -e

if [ $OJ_STATUS -eq 0 ]; then
    exit 0
fi

echo "oj submit failed. This is likely due to AtCoder's Turnstile security blocking the automated tool."
echo "Falling back to Manual Browser Submission..."

# Copy code to Windows clipboard
cat "$FILE" | clip.exe
echo "✅ Code copied to clipboard!"

# Open submission page
SUBMIT_URL="${TASK_URL%/tasks/*}/submit"
echo "Opening submission page: $SUBMIT_URL"
explorer.exe "$SUBMIT_URL"

echo "👉 Paste (Ctrl+V) code and click Submit in the browser."
exit 1
