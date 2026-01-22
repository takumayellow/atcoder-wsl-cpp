#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

/**
 * @brief プログラムのエントリーポイント
 * 
 * 標準入力から2つの整数n（総数）とw（1単位あたりの量）を読み取り、
 * n÷wの商（整数除算）を標準出力に出力します。
 * 
 * @return int プログラムの終了ステータス（0: 正常終了）
 * 
 * @details
 * - ios::sync_with_stdio(false): C++の入出力とCの入出力の同期を無効化し、高速化
 * - cin.tie(nullptr): cinとcoutの結びつきを解除し、入出力のバッファリングを最適化
 *   nullptrは型安全なヌルポインタ定数で、従来のNULLや0よりも推奨される
 * - 整数除算により、小数点以下は切り捨てられる
 */
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, w;
    cin >> n >> w;;

    printf("%d\n", n/w);

    return 0;
}
