#!/bin/bash
set -e

# Determine ACL path (relative to repo root, assuming structure contest/problem/)
REPO_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || echo "../../")
ACL_PATH="$REPO_ROOT/ac-library"

if [ ! -d "$ACL_PATH" ]; then
    # Fallback to home dir standard
    ACL_PATH="$HOME/AtCoderSolution/ac-library"
fi

# 実行のたびにソースを .snap/<日時>_<ok|ng|ce>.<拡張子> に写しておく。
# 解き終わってから「何時何分にどのコードで何が起きたか」を振り返るための記録
# （solve-retro スキルが使う）。前回と同じ内容なら写さない。ACTEST_SNAPSHOT=0 で止まる。
# 写せなくてもテストの結果は変えない（警告だけ出す）。
snapshot() {
    local src=$1 verdict=$2
    [ "${ACTEST_SNAPSHOT:-1}" = 0 ] && return 0
    local ext=${src##*.}
    mkdir -p .snap 2>/dev/null || { echo "actest: .snap を作れないので記録しない" >&2; return 0; }
    local last
    last=$(ls -1 .snap/*."$ext" 2>/dev/null | tail -n 1)
    if [ -n "$last" ] && cmp -s "$src" "$last"; then
        return 0
    fi
    cp "$src" ".snap/$(date +%Y%m%d-%H%M%S)_${verdict}.${ext}" || echo "actest: .snap に記録できなかった" >&2
}

# テストを走らせ、結果に合わせてスナップショットを残す。終了コードはテストのものを返す
run_tests() {
    local src=$1
    shift
    local status=0
    "$@" || status=$?
    if [ "$status" -eq 0 ]; then
        snapshot "$src" ok
    else
        snapshot "$src" ng
    fi
    return "$status"
}

if [ -f "main.cpp" ]; then
    echo "Testing C++ (main.cpp)..."
    # Use -I for include path. WSL g++ usually fine.
    if ! g++ -std=c++17 -Wall -I "$ACL_PATH" main.cpp -o a.out; then
        snapshot main.cpp ce
        exit 1
    fi
    run_tests main.cpp oj t -c "./a.out"
elif [ -f "main.py" ]; then
    echo "Testing Python (main.py)..."
    run_tests main.py oj t -c "python3 main.py"
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
    if ! "$DOTNET" build -c Release -o bin/oj -v q --nologo; then
        snapshot main.cs ce
        exit 1
    fi
    run_tests main.cs oj t -c "$EXE"
else
    echo "Error: No main.cpp / main.py / main.cs found in current directory."
    exit 1
fi
