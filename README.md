# AtCoderSolution (WSL Ubuntu / C++23)

WSL(Ubuntu) 上の AtCoder 用 C++ テンプレです。  
g++-12 / GDB / ac-library / oj / acc / VS Code 設定(.vscode)を同梱。

## 🔑 最短フロー
1) 初回だけログイン
   acc login
   oj login https://atcoder.jp/
2) 開く（ワンコマンド）
   acx <contest-id> [a|b|c|...]
   例: acx abc364 a  → 雛形が無ければ作成→ VS Code で a/main.cpp を開く
   メモ: 直近の contest は ~/.config/acx/last に記憶。acx b だけでB問題を開ける
3) VS Code のキー
   ビルド: Ctrl+Alt+B / テスト: Ctrl+Alt+T / 提出: Ctrl+Alt+S / デバッグ: F5

## 🧭 acx コマンド
acx            : 直近コンテストの A を開く
acx b          : 直近コンテストの B を開く
acx abc364 c   : 指定コンテストの C を開く（無ければ acc new 実行）

## 📁 構成
AtCoderSolution/
 ├ .vscode/（ビルド/デバッグ/コマンド）
 ├ ac-library/（ACL）
 ├ abc***/（acc new で作られる各問題）
 ├ tools/acx（ワンコマンド起動）
 └ debug.in, README.md

## 困ったら
- PowerShell ではなく **Ubuntu(WSL)** で実行
- `oj/acc` が見つからない → `source ~/.bashrc` → `which oj` / `which acc`
