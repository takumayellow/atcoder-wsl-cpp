#!/usr/bin/env bash
set -euo pipefail

# Guard: require WSL bash
if [ -z "${WSL_DISTRO_NAME-}" ]; then
  echo "This script must be run inside WSL (Ubuntu) bash."
  exit 1
fi

sudo apt-get update -y
sudo apt-get install -y build-essential git curl unzip xclip ca-certificates pkg-config gdb gcc-12 g++-12

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12

# pyenv + Python 3.10（oj 用）
sudo apt-get install -y make libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libffi-dev liblzma-dev
[ -d "$HOME/.pyenv" ] || git clone https://github.com/pyenv/pyenv.git ~/.pyenv
if ! grep -q 'pyenv init' ~/.bashrc; then
  cat <<'EOF' >> ~/.bashrc

# --- pyenv ---
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
EOF
fi
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv install -s 3.10.14
pyenv global 3.10.14
python -m pip install --upgrade pip
python -m pip install --user -U online-judge-tools online-judge-api-client
grep -q '\.local/bin' ~/.bashrc || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
export PATH="$HOME/.local/bin:$PATH"

# nvm + acc
export NVM_DIR="$HOME/.nvm"
[ -d "$NVM_DIR" ] || curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
. "$NVM_DIR/nvm.sh"
nvm install --lts
npm install -g atcoder-cli

# ACL（なければ取得）
if [ ! -d "$HOME/AtCoderSolution/ac-library" ]; then
  cd "$HOME/AtCoderSolution"
  curl -fsSL https://github.com/atcoder/ac-library/archive/refs/heads/master.zip -o acl.zip
  unzip -q acl.zip && rm acl.zip
  mv ac-library-master ac-library
fi

echo "Setup done."
