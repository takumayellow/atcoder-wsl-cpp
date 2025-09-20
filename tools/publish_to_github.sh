#!/usr/bin/env bash
set -euo pipefail

# Usage: bash tools/publish_to_github.sh [repo_name] [private|public]
REPO="${1:-AtCoderSolution}"
VISIBILITY="${2:-private}"

cd "$(dirname "$0")"/..

# include ACL in repo (ensure not ignored)
if grep -q '^ac-library/\*\*' .gitignore 2>/dev/null; then
  sed -i '/^ac-library\/\*\*/d' .gitignore
fi

git init -b main 2>/dev/null || true
git add .
git commit -m "Initial commit: WSL C++23 env + ACL + VSCode tasks + docs" 2>/dev/null || true

if ! command -v gh >/dev/null 2>&1; then
  sudo apt-get update -y && sudo apt-get install -y gh
fi

gh auth status >/dev/null 2>&1 || gh auth login -p https -w

USER="$(gh api user --jq .login)"
if gh repo view "$USER/$REPO" >/dev/null 2>&1; then
  echo "Repo $USER/$REPO already exists. Pushing to it..."
  git remote remove origin 2>/dev/null || true
  gh repo set-default "$USER/$REPO" 2>/dev/null || true
  git remote add origin "https://github.com/$USER/$REPO.git"
  git push -u origin main
else
  gh repo create "$USER/$REPO" --source=. --remote=origin --"$VISIBILITY" --push
fi

echo "Done. Repository: https://github.com/$USER/$REPO"
