# AtCoder Solution (WSL / C++ & Python)

このリポジトリは、WSL上でAtCoderの問題を解くための環境です。
C++ (ac-library対応) と Python の両方に対応しており、コマンド一つで環境構築やテストが可能です。

## セットアップ

WSL内のターミナルで以下を実行し、初期設定を行います（初回のみ）。

```bash
# atcoder-cli (acc) の設定とテンプレートのインストール
./tools/setup_env.sh
```

## 使い方（Windows / Cursor / PowerShell）

### 1. 問題の準備

PowerShellまたはCursorのターミナルで:

```powershell
# ABC231のA問題を開く（C++）
.\acx.bat abc231 a

# Pythonで解く場合
.\acx.bat abc231 a py

# 前回と同じコンテストの別問題
.\acx.bat b
```

コンテストフォルダが自動作成され、`main.cpp`（または`main.py`）が現在のCursorウィンドウで開きます。

### 2. コーディング

開いたファイルにコードを書きます。

### 3. テスト実行

問題のディレクトリ（例: `abc231\a`）に移動してから:

```powershell
# リポジトリルートからの相対パスで実行
..\..\test.bat

# または、リポジトリルートから絶対パス指定
C:\Users\takum\Documents\atcoder\atcoder-wsl-cpp\test.bat
```

### 4. 提出

```powershell
..\..\submit.bat
```

## 使い方（WSL内から直接）

WSLターミナル内でも同様に使えます。

```bash
# 問題の準備
./tools/acx abc231 a

# テスト
cd abc231/a
../../tools/test_code.sh

# 提出
acc s
```

## フォルダ構成

```
atcoder-wsl-cpp/
├── abcXXX/           # コンテストごとの作業フォルダ
│   └── a/            # 問題ごとのフォルダ
│       ├── main.cpp  # ソースコード
│       └── test/     # サンプルケース
├── ac-library/       # AtCoder Library (C++用)
├── tools/
│   ├── acx           # コンテスト準備スクリプト (WSL用)
│   ├── setup_env.sh  # 環境構築用スクリプト
│   ├── test_code.sh  # テスト実行用スクリプト
│   └── templates/    # C++ / Python のテンプレートファイル
├── acx.bat           # Windows用ラッパー（問題準備）
├── test.bat          # Windows用ラッパー（テスト）
└── submit.bat        # Windows用ラッパー（提出）
```

## 依存ツール

- WSL (Ubuntu推奨)
- g++ (C++17以上)
- Python 3
- atcoder-cli (acc)
- online-judge-tools (oj)
