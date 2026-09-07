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
    oj t -c "./a.out"
elif [ -f "main.py" ]; then
    echo "Testing Python (main.py)..."
    oj t -c "python3 main.py"
elif [ -f "main.cs" ]; then
    echo "Testing C# (main.cs)..."
    # WSL には .NET SDK を入れていないので、Windows 側の dotnet.exe を使う。
    # 生成される main.exe は WSL の interop からそのまま実行できる。
    if command -v dotnet >/dev/null 2>&1; then
        DOTNET=dotnet
        EXE=./bin/oj/main
    else
        DOTNET=dotnet.exe
        EXE=./bin/oj/main.exe
    fi
    "$DOTNET" build -c Release -o bin/oj -v q --nologo
    oj t -c "$EXE"
else
    echo "Error: No main.cpp / main.py / main.cs found in current directory."
    exit 1
fi
