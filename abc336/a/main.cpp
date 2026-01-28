#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

/**
 * @brief AtCoder ABC336 問題 A のメイン関数。
 * 
 * このプログラムは標準入力から整数 n を読み取り、"Long" の文字列に n 個の 'o' を 'L' と 'ng' の間に挿入して出力します。
 * 例えば、n=2 の場合、"Loong" を出力します。
 * 
 * string(n, 'o') で 'o' をシングルクォートで囲んでいるのは、'o' が文字リテラル (char 型) であり、
 * string コンストラクタがサイズと char を引数に取るためです。ダブルクォートは文字列リテラル (const char*) を表し、ここでは互換性がありません。
 * 
 * @return int 正常終了時に 0 を返します。
 */
/**
 * @brief 標準入力から整数 n を読み取り、文字列を出力するメイン関数。
 * 
 * プログラムは整数 n を読み取り、以下の文字列を構築して出力します：
 * - 文字 'L'
 * - 次に n 回繰り返した文字 'o'
 * - 最後に文字列 "ng"
 * 
 * これにより、"Long"、"Loong" などの単語を入力値に基づいて生成します。
 * 
 * @return int 正常終了時に 0 を返します。
 */
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >>n;
    cout << ("L" + string(n, 'o') + "ng") << "\n";

    return 0;
}
