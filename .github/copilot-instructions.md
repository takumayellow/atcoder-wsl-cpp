# AtCoder Competitive Programming Environment

This is a WSL-based development environment for solving AtCoder problems in C++ and Python, with integrated tools for testing and submission.

## Architecture Overview

- **Contest Structure**: Each contest (e.g., `abc231/`) contains `contest.acc.json` and problem subdirectories (e.g., `a/`, `b/`).
- **Problem Structure**: Each problem directory has `main.cpp` or `main.py` for the solution, and `test/` with sample input/output files.
- **Library Integration**: C++ code uses AtCoder Library (`ac-library/`) for competitive programming utilities.
- **Tooling**: Custom scripts (`acx`, `actest`, `acsub`) automate problem setup, testing with `oj` (online-judge-tools), and submission via `acc` (atcoder-cli).

## Key Workflows

### Problem Solving Workflow
1. **Open Problem**: Run `acx <contest-id> <problem>` (e.g., `acx abc231 a`) to create directory, download samples, and open template in editor.
2. **Edit Code**: Modify `main.cpp` or `main.py` in the problem directory.
3. **Test Locally**: Run `actest` in the problem directory to compile (C++) and test against samples using `oj t`.
4. **Submit**: Run `acsub` to submit code to AtCoder.

### Build and Test Commands
- **C++ Compilation**: `g++ -std=c++17 -Wall -I <repo-root>/ac-library main.cpp -o a.out`
- **Testing**: `oj t -c "./a.out"` (C++) or `oj t -c "python3 main.py"` (Python)
- **Submission**: `acc submit` (preferred) or `oj submit` as fallback

## Code Patterns

### C++ Template (see `tools/templates/cpp/main.cpp`)
```cpp
#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Solution code here
    
    return 0;
}
```
- Always include `<atcoder/all>` for library access.
- Use `ios::sync_with_stdio(false); cin.tie(nullptr);` for fast I/O.
- Define `using ll = long long;` for convenience.

### Python Template (see `tools/templates/python/main.py`)
```python
import sys

def solve():
    # Solution code here
    pass

if __name__ == '__main__':
    solve()
```
- Keep input handling simple; `oj` handles stdin/stdout piping.

## Dependencies and Setup
- Requires WSL2 with g++, Python3, Node.js.
- Install `atcoder-cli` (acc) and `online-judge-tools` (oj).
- Login to AtCoder via `oj login` and `acc login`.

## Key Files
- `tools/acx`: Problem opener script.
- `tools/test_code.sh`: Testing logic.
- `ac-library/`: AtCoder C++ library headers.
- `tools/templates/`: Code templates for new problems.</content>
<parameter name="filePath">c:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\.github\copilot-instructions.md