#!/usr/bin/env bash
set -euo pipefail
USR="$HOME/.vscode-server/data/Machine"; mkdir -p "$USR"
cat > "$USR/keybindings.json" <<'JSON'
[
  { "key": "ctrl+alt+b", "command": "workbench.action.tasks.build" },
  { "key": "ctrl+alt+t", "command": "command-runner.run", "args": "oj test" },
  { "key": "ctrl+alt+s", "command": "command-runner.run", "args": "acc submit" }
]
JSON
echo "Keybindings installed. Reload VS Code to apply."
