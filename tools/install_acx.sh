#!/usr/bin/env bash
set -euo pipefail
chmod +x "${HOME}/AtCoderSolution/tools/acx" 2>/dev/null || true
mkdir -p "${HOME}/.local/bin"
ln -sf "${HOME}/AtCoderSolution/tools/acx" "${HOME}/.local/bin/acx"
grep -q '\.local/bin' "${HOME}/.bashrc" || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "${HOME}/.bashrc"
echo "Installed: acx. Re-open terminal or: source ~/.bashrc"
