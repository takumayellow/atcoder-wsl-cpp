
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

chmod +x "${REPO_ROOT}/tools/acx" 2>/dev/null || true
chmod +x "${REPO_ROOT}/tools/test_code.sh" 2>/dev/null || true
chmod +x "${REPO_ROOT}/tools/submit_code.sh" 2>/dev/null || true
chmod +x "${REPO_ROOT}/actest" 2>/dev/null || true
chmod +x "${REPO_ROOT}/acsub" 2>/dev/null || true
mkdir -p "${HOME}/.local/bin"
ln -sf "${REPO_ROOT}/tools/acx" "${HOME}/.local/bin/acx"
ln -sf "${REPO_ROOT}/actest" "${HOME}/.local/bin/actest"
ln -sf "${REPO_ROOT}/acsub" "${HOME}/.local/bin/acsub"
grep -q '\.local/bin' "${HOME}/.bashrc" || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "${HOME}/.bashrc"
echo "Installed: acx, actest, acsub. Re-open terminal or: source ~/.bashrc"
