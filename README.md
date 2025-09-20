# AtCoderSolution (WSL Ubuntu / C++23)

WSL(Ubuntu) 上に AtCoder 用の C++ 環境を用意したテンプレです。  
- **g++-12 (C++23)** / **GDB**
- **online-judge-tools (oj)**、**atcoder-cli (acc)**
- **AtCoder Library (ac-library)** 同梱
- **VS Code** タスク/デバッグ設定（`.vscode/`）

## 初回セットアップ（未実行なら）
WSL の Ubuntu ターミナルで：
```bash
bash tools/setup_wsl.sh
```

## 初回ログイン
```bash
acc login
oj login https://atcoder.jp/
```

## 使い方
### 1) コンテスト雛形
```bash
cd ~/AtCoderSolution
acc new abcXXXX
cd abcXXXX/a
```

### 2) ビルド
- VS Code: `Ctrl+Shift+B`（タスク: **c++ build for AtCoder**）
- 直接: `g++ -std=gnu++23 -I "$HOME/AtCoderSolution/ac-library" main.cpp -o "$HOME/AtCoderSolution/a.out"`

### 3) サンプルテスト
```bash
oj test -S -N -c "$HOME/AtCoderSolution/a.out" -d test
```

### 4) 提出
```bash
acc submit main.cpp
```

### 5) デバッグ
- `F5` で `debug.in` を標準入力として実行（`launch.json` 済み）
