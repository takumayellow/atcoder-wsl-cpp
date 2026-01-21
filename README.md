# AtCoder Solution (WSL / C++ & Python)

Windows + WSL環境でAtCoderの問題を解くための統合開発環境です。

- **C++**: ac-library対応、高速I/O設定済み
- **Python**: Python3対応
- **エディタ連携**: VS Code / Cursor から直接操作可能
- **自動化**: 問題フォルダ作成、サンプルケーステスト、提出まで一括管理

---

## 目次

1. [初期セットアップ](#初期セットアップ)
2. [使い方](#使い方)
3. [コマンドリファレンス](#コマンドリファレンス)
4. [ワークフロー例](#ワークフロー例)
5. [フォルダ構成](#フォルダ構成)
6. [トラブルシューティング](#トラブルシューティング)
7. [技術詳細](#技術詳細)

---

## 初期セットアップ

### 前提条件

- Windows 10/11
- WSL2 (Ubuntu推奨)
- VS Code または Cursor
- WSL内に以下がインストール済み:
  - g++ (C++17以上)
  - Python 3
  - Node.js (nvm経由推奨)

### Step 1: WSL環境の構築

WSLターミナルで以下を実行:

```bash
# リポジトリのルートに移動
cd /mnt/c/Users/takum/Documents/atcoder/atcoder-wsl-cpp

# 依存ツールのインストールとテンプレート設定
./tools/setup_wsl.sh    # 初回のみ: acc, oj のインストール
./tools/setup_env.sh    # テンプレートの登録
```

### Step 2: AtCoderへのログイン

WSLターミナルで:

```bash
# online-judge-tools でログイン
oj login https://atcoder.jp/

# atcoder-cli でログイン
acc login
```

> **注意**: ターミナルでのパスワード入力がうまくいかない場合は、Seleniumを使ったブラウザ認証か、Chromeのcookieを手動でコピーする方法があります（後述）。

### Step 3: PowerShellエイリアスの設定（推奨）

PowerShellプロファイルを編集して、どこからでもコマンドを使えるようにします。

```powershell
# プロファイルを開く
notepad $PROFILE
```

以下を追記:

```powershell
# ========== AtCoder Tools ==========
$ACX_ROOT = "C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp"

function Invoke-Acx {
    & "$ACX_ROOT\acx.bat" @args
}
Set-Alias acx Invoke-Acx

function Invoke-AcTest {
    & "$ACX_ROOT\test.bat" @args
}
Set-Alias actest Invoke-AcTest

function Invoke-AcSubmit {
    & "$ACX_ROOT\submit.bat" @args
}
Set-Alias acsub Invoke-AcSubmit
```

保存後、新しいターミナルを開くか以下を実行:

```powershell
. $PROFILE
```

---

## 使い方

### 基本の流れ

```powershell
# 1. 問題を開く（フォルダ作成 + エディタでファイルを開く）
acx abc231 a

# 2. コードを書く（main.cpp を編集）

# 3. 問題ディレクトリに移動
cd C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\abc231\a

# 4. サンプルケースでテスト
actest

# 5. 提出
acsub
```

### エディタの自動検出

`acx` コマンドは実行元の環境を自動検出します:

| 実行元 | 開くエディタ |
|--------|-------------|
| VS Codeのターミナル | VS Code |
| Cursorのターミナル | Cursor |
| 通常のPowerShell | 利用可能なエディタ |

---

## コマンドリファレンス

### `acx` - 問題を開く

```powershell
acx <contest-id> <problem> [py]
```

| 引数 | 説明 |
|------|------|
| `contest-id` | コンテストID（例: `abc231`, `arc150`） |
| `problem` | 問題ID（例: `a`, `b`, `c`, `d`, `e`, `f`, `g`） |
| `py` | Python で解く場合に指定（省略時はC++） |

**例:**

```powershell
acx abc231 a        # ABC231-A を C++ で開く
acx abc231 a py     # ABC231-A を Python で開く
acx b               # 前回のコンテストの B問題 を開く
acx c py            # 前回のコンテストの C問題 を Python で開く
```

**動作:**
1. コンテストフォルダが無ければ `acc new` で作成（サンプルケースも自動ダウンロード）
2. テンプレートから `main.cpp` または `main.py` を生成
3. 現在のエディタでファイルを開く

### `actest` - テスト実行

```powershell
actest
```

現在のディレクトリにある `main.cpp` または `main.py` を自動判別してテストを実行します。

**動作:**
- C++: `g++ -std=c++17 -Wall -I <ac-library> main.cpp` でコンパイル後、`oj t` でテスト
- Python: `oj t -c "python3 main.py"` でテスト

**online-judge-tools (oj) の挙動:**
- `oj t` はカレントディレクトリ配下の `test/` にあるサンプルケースを実行します
- `acc new` で生成した問題フォルダには `test/` が自動作成されます
- `test/` が無い場合はテストが走らないため、必要なら `oj d <url>` で取得します
- この環境では `oj` は WSL 内で動作し、`actest`/VS Code タスクから WSL に渡しています

### `acsub` - 提出

```powershell
acsub
```

現在のディレクトリのコードをAtCoderに提出します（`acc submit` を実行）。

---

## ワークフロー例

### ABC231 A問題を解く

```powershell
# 1. 問題を開く
PS> acx abc231 a
Ready in /mnt/c/Users/takum/Documents/atcoder/atcoder-wsl-cpp/abc231/a
Opening: C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\abc231\a\main.cpp

# 2. エディタで main.cpp を編集
#    （自動で開かれる）

# 3. 問題ディレクトリに移動
PS> cd C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\abc231\a

# 4. テスト
PS> actest
Testing C++ (main.cpp)...
[INFO] sample-1: AC (0.01s)
[INFO] sample-2: AC (0.01s)
[SUCCESS] All tests passed!

# 5. 提出
PS> acsub
```

### Pythonで解く場合

```powershell
acx abc231 a py
cd C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\abc231\a
# main.py を編集
actest
acsub
```

---

## フォルダ構成

```
atcoder-wsl-cpp/
│
├── acx.bat              # Windows用: 問題を開く
├── test.bat             # Windows用: テスト実行
├── submit.bat           # Windows用: 提出
│
├── tools/
│   ├── acx              # WSL用: メインスクリプト
│   ├── setup_wsl.sh     # WSL環境構築（acc, oj インストール）
│   ├── setup_env.sh     # テンプレート登録
│   ├── test_code.sh     # テスト実行スクリプト
│   └── templates/
│       ├── cpp/
│       │   ├── main.cpp        # C++ テンプレート
│       │   └── template.json   # acc設定
│       └── python/
│           ├── main.py         # Python テンプレート
│           └── template.json   # acc設定
│
├── ac-library/          # AtCoder Library (C++用)
│
├── abc231/              # コンテストフォルダ（自動生成）
│   ├── contest.acc.json
│   └── a/
│       ├── main.cpp     # ソースコード
│       └── test/        # サンプルケース
│           ├── sample-1.in
│           ├── sample-1.out
│           └── ...
│
└── README.md
```

---

## トラブルシューティング

### `acx` コマンドが見つからない

PowerShellプロファイルが読み込まれていません:

```powershell
. $PROFILE
```

または、直接batファイルを実行:

```powershell
C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\acx.bat abc231 a
```

### `acc: command not found`

WSL内でNode.jsのパスが通っていません:

```bash
# NVMを読み込む
source ~/.nvm/nvm.sh

# または、パスを直接追加
export PATH="$HOME/.nvm/versions/node/v22.19.0/bin:$PATH"
```

### ログインできない（Username or Password is incorrect）

ターミナルでの対話入力がうまくいかない場合があります。

**解決策1: Selenium を使う**

```bash
pip install selenium
oj login https://atcoder.jp/
```

ブラウザが起動してログインできます。

**解決策2: Chromeのcookieを手動コピー**

1. ChromeでAtCoderにログイン
2. 拡張機能「EditThisCookie」でcookieをエクスポート
3. `cookie.json` として保存
4. 以下のスクリプトで変換:

```python
import json
import http.cookiejar

with open('cookie.json', 'r') as f:
    data = json.load(f)

cj = http.cookiejar.LWPCookieJar('cookie.jar')

for x in data:
    c = http.cookiejar.Cookie(
        version=0, name=x['name'], value=x['value'],
        port=None, port_specified=False,
        domain=x['domain'], domain_specified=True,
        domain_initial_dot=x['domain'].startswith('.'),
        path=x['path'], path_specified=True,
        secure=x['secure'], expires=x.get('expirationDate'),
        discard=False, comment=None, comment_url=None,
        rest={'HttpOnly': x.get('httpOnly')}, rfc2109=False
    )
    cj.set_cookie(c)

cj.save()
print('cookie.jar created')
```

5. WSLの所定の場所にコピー:

```bash
cp cookie.jar ~/.local/share/online-judge-tools/cookie.jar
```

### テストケースがダウンロードされない

手動でダウンロード:

```bash
cd abc231/a
oj d https://atcoder.jp/contests/abc231/tasks/abc231_a
```

### 別のウィンドウでエディタが開いてしまう

`acx.bat` は実行元のエディタを検出して同じエディタで開くようになっています。
検出がうまくいかない場合は、環境変数 `TERM_PROGRAM` を確認してください。

---

## 技術詳細

### テンプレート (C++)

```cpp
#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // write code here

    return 0;
}
```

### テンプレート (Python)

```python
import sys

# sys.setrecursionlimit(2000)

def solve():
    # input = sys.stdin.read
    # data = input().split()
    pass

if __name__ == '__main__':
    solve()
```

### 依存ツール

| ツール | 説明 | インストール |
|--------|------|-------------|
| WSL2 | Windows Subsystem for Linux | `wsl --install` |
| g++ | C++コンパイラ | `sudo apt install g++` |
| Python3 | Python実行環境 | `sudo apt install python3` |
| Node.js | acc の実行に必要 | `nvm install --lts` |
| atcoder-cli (acc) | AtCoder用CLI | `npm install -g atcoder-cli` |
| online-judge-tools (oj) | テスト・提出ツール | `pip install online-judge-tools` |

### パス変換

Windows ↔ WSL のパス変換:
- `C:\Users\takum\...` → `/mnt/c/Users/takum/...`
- `/mnt/c/Users/takum/...` → `C:\Users\takum\...`

`acx.bat` 内で自動変換しています。

---

## ライセンス

MIT License
