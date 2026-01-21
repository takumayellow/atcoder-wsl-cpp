# AtCoder Solution (WSL / C++ & Python)

このリポジトリは、WSL上でAtCoderの問題を解くための環境です。
C++ (ac-library対応) と Python の両方に対応しており、コマンド一つで環境構築やテストが可能です。

## 🚀 セットアップ

WSL内のターミナルで以下を実行し、初期設定を行います（初回のみ）。

```bash
# atcoder-cli (acc) の設定とテンプレートのインストール
./tools/setup_env.sh
```

## 📝 使い方

### 1. 問題の準備 (`acx` コマンド)

`tools/acx` スクリプトを使って、コンテスト用フォルダの作成とファイルを開く操作を自動化できます。
PATHを通すか、aliasを設定すると便利です（例: `alias acx=./tools/acx`）。

```bash
# 基本: C++で直近のコンテストのA問題を開く
./tools/acx abc364 a

# Pythonでやりたい場合
./tools/acx abc364 a py

# 問題指定のみ（前回開いたコンテストのB問題を開く）
./tools/acx b
```

### 2. コーディング

作成されたフォルダ（例: `abc364/a/`）内の `main.cpp` または `main.py` を編集します。
`tools/templates/` 内のファイルがテンプレートとして使用されます。

### 3. テストの実行 (`test_code.sh`)

問題のディレクトリ内で以下のコマンドを実行すると、サンプルケースのテストが行われます。
言語（C++かPythonか）は自動判定されます。

```bash
# 例: abc364/a/ に移動してから
../../tools/test_code.sh
```

### 4. 提出

```bash
acc s
```

## 📁 フォルダ構成

- `abcXXX/` : コンテストごとの作業フォルダ
- `ac-library/` : AtCoder Library (C++用)
- `tools/`
  - `acx` : コンテスト準備・エディタ起動用スクリプト
  - `setup_env.sh` : 環境構築用スクリプト
  - `test_code.sh` : テスト実行用スクリプト
  - `templates/` : C++ / Python のテンプレートファイル

## 🛠 依存ツール
- WSL (Ubuntu推奨)
- g++ (C++17以上)
- Python 3
- atcoder-cli (acc)
- online-judge-tools (oj)
