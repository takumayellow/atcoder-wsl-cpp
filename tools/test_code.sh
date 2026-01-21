#!/bin/bash
set -e

# Determine ACL path (relative to repo root, assuming structure contest/problem/)
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo "../../")
ACL_PATH="$REPO_ROOT/ac-library"

if [ ! -d "$ACL_PATH" ]; then
    # Fallback to home dir standard
    ACL_PATH="$HOME/AtCoderSolution/ac-library"
fi

if [ -f "main.cpp" ]; then
    echo "Testing C++ (main.cpp)..."
    # Use -I for include path. WSL g++ usually fine.
    g++ -std=c++17 -Wall -I "$ACL_PATH" main.cpp -o a.out
.\acx.bat abc231 a
    oj t -c "./a.out"
elif [ -f "main.py" ]; then
    echo "Testing Python (main.py)..."
    oj t -c "python3 main.py"
else
    echo "Error: No main.cpp or main.py found in current directory."
    exit 1
fi
