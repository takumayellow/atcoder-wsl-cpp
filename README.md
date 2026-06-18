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
cd /mnt/c/Users/takum/dev/atcoder/atcoder-wsl-cpp

# 依存ツールのインストールとテンプレート設定
./tools/setup_wsl.sh    # 初回のみ: acc, oj のインストール
./tools/setup_env.sh    # テンプレートの登録
./tools/install_acx.sh  # acx/actest/acsub を PATH に追加
```

### Step 2: AtCoderへのログイン（Cookieコピー方式が正攻法）

> **重要**: 2024年以降、AtCoder は Cloudflare Turnstile によるセキュリティ強化を導入しており、
> **`oj login` / `acc login` の対話ログイン（ユーザー名・パスワード入力）は弾かれます**。
> ユーザー名・パスワードが正しくても失敗するので、これは**正常な挙動**です。
> 代わりに、ブラウザでログイン済みの Cookie を `oj` と `acc` の両方へ流し込みます。

**手順:**

1. **ブラウザでAtCoderにログイン**
   PCのChrome等で https://atcoder.jp/ にログインしておきます。

2. **Cookieをエクスポート**
   拡張機能「EditThisCookie」などで、`atcoder.jp` の Cookie を **JSON形式**でエクスポート（コピー）します。
   最低限 `REVEL_SESSION` が含まれていればOKです。

3. **cookie.json を作成**
   リポジトリ直下（`atcoder-wsl-cpp/`）に `cookie.json` という名前で保存し、JSONを貼り付けます。

4. **両ツールへ反映**
   WSLターミナルで以下を実行します。これで `oj`（cookie.jar）と `acc`（session.json）の**両方**に
   セッションが書き込まれます。
   ```bash
   ./tools/update_cookie.sh
   ```

5. **ログイン確認**
   ```bash
   oj login --check https://atcoder.jp/   # => [SUCCESS] You have already signed in.
   acc session                            # => check login status... OK
   ```

> **セッションの有効期限について**: コピーした Cookie（`REVEL_SESSION`）には有効期限があります。
> ある日突然 `oj`/`acc` がログイン切れになったら、**2〜5 を再実行**（cookie.json を再エクスポートして
> `./tools/update_cookie.sh`）してください。`update_cookie.sh` はリポジトリの場所を自動検出するので、
> リポジトリを移動しても編集不要です。

> **補足（提出時の× Error）**: 上記でログインできていても、`oj submit` 自体が Turnstile で
> 弾かれて「× Error」になる場合があります。その場合は `acsub` が自動でコードをクリップボードへ
> コピーし提出ページをブラウザで開くので、**Ctrl+V → 提出ボタン**で手動提出してください
> （[acsub の制約](#acsub---提出) 参照）。

### Step 3: PowerShellエイリアスの設定（推奨）

PowerShellプロファイルを編集して、どこからでもコマンドを使えるようにします。

```powershell
# プロファイルを開く
notepad $PROFILE
```

以下を追記:

```powershell
# ========== AtCoder Tools ==========
$ACX_ROOT = "C:\Users\takum\dev\atcoder\atcoder-wsl-cpp"

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
cd C:\Users\takum\dev\atcoder\atcoder-wsl-cpp\abc231\a

# 4. サンプルケースでテスト
actest

# 5. 提出
acsub
```

### VS Code ショートカット（推奨）

ターミナルを開かずに実行できて便利です。

#### 1. タスクの自動実行
- **テスト (`Ctrl` + `Shift` + `T`)**:  
  現在開いているファイルをビルドし、自動的にサンプルケースのテストを実行します。

- **提出 (`Alt` + `S`)**:  
  現在開いているファイルを AtCoder に提出します。

#### 2. ショートカットの設定方法
提出コマンド (`Alt + S`) を有効にするには、VS Code でキー割り当てを追加してください。

1. `Ctrl` + `Shift` + `P` → `Preferences: Open Keyboard Shortcuts (JSON)` を選択
2. 以下を追記:
   ```json
    {
        "key": "alt+s",
        "command": "workbench.action.tasks.runTask",
        "args": "S: Submit code (acsub)"
    }
   ```
   ※ `Ctrl+Shift+T` はデフォルトの「テストタスクの実行」に割り当て済みです。

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

現在のディレクトリのコードをAtCoderに提出します。

**⚠️ 現在の制約 (Cloudflare Turnstile):**
AtCoderのセキュリティ強化により、コマンドラインツール(`oj submit`)からの自動提出はブロックされ「× Error」となるケースがほとんどです。
そのため、`acsub` は現在以下の動作を行います：

1. 自動提出を試みる（成功すれば完了）
2. **失敗時（Error発生時）:**
   - コードをクリップボードに自動コピー (`clip.exe`)
   - 該当問題の提出ページをブラウザで開く (`explorer.exe`)
   - ユーザーは **Ctrl+V** で貼り付けて「提出」ボタンを押すだけ

**提出言語のデフォルト:**
- C++ は言語ID `6017`（C++23 GCC）を指定して submit します
- Python は言語ID `6082`（CPython 3.13.7）を指定して submit します


---

## ワークフロー例

### ABC231 A問題を解く

```powershell
# 1. 問題を開く
PS> acx abc231 a
Ready in /mnt/c/Users/takum/dev/atcoder/atcoder-wsl-cpp/abc231/a
Opening: C:\Users\takum\dev\atcoder\atcoder-wsl-cpp\abc231\a\main.cpp

# 2. エディタで main.cpp を編集
#    （自動で開かれる）

# 3. 問題ディレクトリに移動
PS> cd C:\Users\takum\dev\atcoder\atcoder-wsl-cpp\abc231\a

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
cd C:\Users\takum\dev\atcoder\atcoder-wsl-cpp\abc231\a
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
C:\Users\takum\dev\atcoder\atcoder-wsl-cpp\acx.bat abc231 a
```

### `acc: command not found`

WSL内でNode.jsのパスが通っていません:

```bash
# NVMを読み込む
source ~/.nvm/nvm.sh

# または、パスを直接追加
export PATH="$HOME/.nvm/versions/node/v22.19.0/bin:$PATH"
```

### ログインできない / `acc login`・`oj login` が失敗する

**まず前提**: 2024年以降、AtCoder の Cloudflare Turnstile により、`acc login` / `oj login` の
**対話ログイン（ユーザー名・パスワード入力）は弾かれます**。ユーザー名・パスワードが正しくても
失敗するのが正常です。対話ログインを直す方法はありません。

**正しい解決策**: [Step 2: AtCoderへのログイン](#step-2-atcoderへのログイン-cookieコピー方式が正攻法) の
**Cookieコピー方式**を使ってください。要約すると:

```bash
# 1. ブラウザでログイン → EditThisCookie で cookie を JSON エクスポート
# 2. リポジトリ直下に cookie.json として保存
# 3. oj と acc の両方へ反映（リポジトリ位置は自動検出）
./tools/update_cookie.sh

# 4. 確認
oj login --check https://atcoder.jp/   # => You have already signed in.
acc session                            # => check login status... OK
```

`update_cookie.sh` が内部で行うこと:
- `convert_cookie.py` で `cookie.json` → `cookie.jar`(LWP形式) に変換し `~/.local/share/online-judge-tools/cookie.jar` へ配置（**oj 用**）
- `cookie.json` から `REVEL_SESSION` / `REVEL_FLASH` を抽出し `acc config-dir`/`session.json` へ書き込み（**acc 用**）

> **注意**: WSL の PATH に Windows 版 npm の `acc`（`/mnt/c/.../AppData/Roaming/npm/acc`）が
> 先頭にいると WSL bash 上で正しく動かない（exit 127）。`update_cookie.sh` は nvm の Linux 版
> `acc` を優先するよう対策済みです。

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
