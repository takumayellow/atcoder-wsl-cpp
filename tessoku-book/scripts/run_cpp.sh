#!/bin/zsh

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: scripts/run_cpp.sh <problem-dir> [input-file]" >&2
  exit 1
fi

problem_dir="$1"
input_file="${2:-}"
source_file="${problem_dir}/main.cpp"

if [[ ! -f "$source_file" ]]; then
  echo "source not found: $source_file" >&2
  exit 1
fi

sdk_root="$(xcrun --show-sdk-path)"
acl_root="/Users/uenoyuuta/atcoder-wsl-cpp/ac-library"
out_file="/tmp/$(echo "$problem_dir" | tr '/' '_').out"

/opt/homebrew/opt/gcc/bin/g++-15 \
  -std=gnu++17 \
  -O2 \
  -Wall \
  -Wextra \
  -isysroot "$sdk_root" \
  -I"$acl_root" \
  "$source_file" \
  -o "$out_file"

if [[ -n "$input_file" ]]; then
  "$out_file" < "$input_file"
else
  "$out_file"
fi
