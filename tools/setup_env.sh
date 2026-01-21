#!/bin/bash
set -e

# Setup PATH for node/acc and oj - specific version as found earlier
export PATH="$HOME/.nvm/versions/node/v22.19.0/bin:$HOME/.local/bin:$PATH"

if ! command -v acc &> /dev/null; then
    echo "acc not found. Please ensure it is installed via setup_wsl.sh"
    exit 1
fi

CONFIG_DIR=$(acc config-dir)
echo "Config dir: $CONFIG_DIR"

# Get Repo Root (assuming script is run from inside repo)
# If run via `wsl ... tools/setup_env.sh`, pwd might be repo root.
REPO_ROOT=$(pwd)
if [ ! -d "$REPO_ROOT/tools/templates" ]; then
    # Try finding it relative to script location if symlinked or executed differently
    SCRIPT_DIR=$(dirname "$(realpath "$0")")
    if [ -d "$SCRIPT_DIR/templates" ]; then
        REPO_ROOT="$SCRIPT_DIR/.."
    fi
fi

if [ ! -d "$REPO_ROOT/tools/templates" ]; then
    echo "Error: Could not find tools/templates directory at $REPO_ROOT/tools/templates"
    exit 1
fi

TEMPLATE_CPP="$REPO_ROOT/tools/templates/cpp"
TEMPLATE_PY="$REPO_ROOT/tools/templates/python"

# Copy templates
mkdir -p "$CONFIG_DIR/cpp"
cp -r "$TEMPLATE_CPP/"* "$CONFIG_DIR/cpp/"
echo "Installed C++ template to $CONFIG_DIR/cpp"

mkdir -p "$CONFIG_DIR/python"
cp -r "$TEMPLATE_PY/"* "$CONFIG_DIR/python/"
echo "Installed Python template to $CONFIG_DIR/python"

# Configure defaults
acc config default-template cpp
acc config default-test-dirname-format test

echo "---------------------------------------------------"
echo "Setup Complete!"
echo "---------------------------------------------------"
echo "Workflow:"
echo "1. Create Contest:  acc new <contest_id>"
echo "   (e.g., acc new abc364)"
echo "   (For Python only: acc new abc364 --template python)"
echo ""
echo "2. Solve Problem:"
echo "   cd <contest_id>/<a>"
echo "   (Edit main.cpp or main.py)"
echo ""
echo "3. Test:"
echo "   oj t -c 'g++ main.cpp && ./a.out'  (for C++)"
echo "   oj t -c 'python3 main.py'          (for Python)"
echo ""
echo "   * Tip: You can define an alias for testing in your .bashrc"
echo ""
echo "4. Submit:"
echo "   acc s"
