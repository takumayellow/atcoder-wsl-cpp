// ICPC 複数データセット入力の雛形（C++）
//
// ICPC は AtCoder と違い「1ファイルに複数データセット」が定番。
// 終端条件は問題ごとに違う。下の A/B/C から問題文に合うものを使う:
//   A) 番兵終端: n が 0（や "0 0"）の行で終わり          ← 国内予選で最頻出
//   B) EOF 終端: 入力が尽きるまで繰り返し
//   C) ケース数: 先頭に T があり、T 個のデータセット
//
// 注意: ACL は標準に無いので、使うなら下の方に該当ヘッダを「貼り付け」て使う
//       （library/cpp/ に抜粋を用意）。

#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i, n) for (int i = 0; i < (n); ++i)

// ---- ここに ACL 抜粋や自前ライブラリを貼り付ける ----
// （例: library/cpp/dsu.hpp の中身をそのまま）

// 1 データセットの処理
void solve(int n) {
    // ... 残りの入力を読んで答えを出力 ...
    (void)n;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // ===== パターンA: 番兵終端（n==0 で終了）=====
    int n;
    while (cin >> n && n != 0) {
        solve(n);
    }

    // ===== パターンB: EOF 終端 =====
    // int a, b;
    // while (cin >> a >> b) {
    //     // ...
    // }

    // ===== パターンC: 先頭にケース数 T =====
    // int T;
    // cin >> T;
    // while (T--) {
    //     // ...
    // }

    return 0;
}
