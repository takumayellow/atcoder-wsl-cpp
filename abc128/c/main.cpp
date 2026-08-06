// ABC128 C - Switches (300点)
// https://atcoder.jp/contests/abc128/tasks/abc128_c
//
// 解法: bit 全探索 O(2^N * M * N)
//   N <= 10 なのでスイッチの ON/OFF の組み合わせは高々 2^10 = 1024 通り。
//   全部作って「M 個の電球が全部点くか」を素直に判定すればよい。
//   詳しい考察は同ディレクトリの explanation.md を参照。

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, M; cin >> N >> M;      // N: スイッチの数 (<=10), M: 電球の数 (<=10)

    // s[i] = 電球 i につながっているスイッチ番号の一覧。
    // vector<vector<int> > の閉じ括弧の間の空白は C++03 互換の書き方（C++11 以降は >> でよい）。
    vector<vector<int> > s(M);
    for (int i = 0; i < M; ++i) {
        int k; cin >> k;                 // 電球 i につながるスイッチの本数
        for (int j = 0; j < k; ++j) {
            int a; cin >> a; --a;        // 入力は 1-indexed。--a で 0-indexed に直す。
                                         // これでスイッチ番号がそのまま bit の位置になる。
            s[i].push_back(a);
        }
    }

    // p[i] = 電球 i が点灯する条件。「つながっている ON スイッチの本数 ≡ p[i] (mod 2)」
    vector<int> p(M);
    for (int i = 0; i < M; ++i) cin >> p[i];

    long long res = 0;                   // 答えは最大 2^10 = 1024 なので int でも足りるが、
                                         // 数え上げの結果は既定で long long にしておくと事故らない。

    // --- bit 全探索 -------------------------------------------------------
    // bit の第 v ビット (0-indexed) が 1 <=> スイッチ v が ON。
    // bit を 0 から 2^N - 1 まで動かすと、ON/OFF の全パターンを重複なく列挙できる。
    for (int bit = 0; bit < (1<<N); ++bit) {
        bool ok = true;                  // この ON/OFF パターンで全電球が点くか

        for (int i = 0; i < M; ++i) {
            int con = 0;                 // 電球 i につながっている ON スイッチの本数
            for (auto v : s[i]) {
                if (bit & (1<<v)) ++con; // v 番のスイッチが ON かをビット判定
            }
            // 偶奇が p[i] と食い違ったら、この電球は点かない → パターン全体が不採用。
            // （break しても正しいが、M<=10 なので最後まで回しても十分速い）
            if (con % 2 != p[i]) ok = false;
        }

        if (ok) ++res;                   // 全電球 OK なら 1 通りとして数える
    }

    cout << res << endl;
}
