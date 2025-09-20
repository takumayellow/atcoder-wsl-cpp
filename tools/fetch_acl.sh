#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"/..
if [ -d ac-library ]; then
  echo "ac-library already exists."
  exit 0
fi
curl -fsSL https://github.com/atcoder/ac-library/archive/refs/heads/master.zip -o acl.zip
unzip -q acl.zip && rm acl.zip
mv ac-library-master ac-library
echo "ac-library fetched."
