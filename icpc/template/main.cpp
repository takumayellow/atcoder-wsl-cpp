// ICPC 国内予選 雛形（C++）: 複数データセットを番兵までループ
//
// 入力は AtCoder と違い「1ファイルに複数データセットが連結」。番兵が来るまで回す。
// cin >> は空白/改行を自動スキップするので行の切れ方は気にしなくてよい。
//   先頭が複数値:  while (cin >> a >> b >> s && (a || b || s))
//   個数T先頭(番兵なし): int T; cin >> T; while (T--) { ... }
// ※ ACL は標準に無い。使うなら library/cpp/ の該当ヘッダを下へ貼り付ける。

#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    while (cin >> n && n != 0) {   // ← 先頭を読む。番兵で終了（問題ごとに変更）
        // ... 1データセットを解いて ans を作る ...
        ll ans = 0;
        cout << ans << "\n";       // 1データセット = 1行
    }
    return 0;
}
