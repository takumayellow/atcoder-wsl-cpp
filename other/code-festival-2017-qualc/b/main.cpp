#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

// 3^n - n(\largepi b_k which is odd)

// b_k (satisfy) の個数はlist bの中で奇数のものがl個のとき2^l上
// 個数をl個としたとき 出力は 2^n-2^l

// 3^n 2^m

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> a(n);
    int count = 0;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 1) count++;
    }
    ll total = 1;
    for (int i = 0; i < n; i++) total *= 3;
    ll all_odd = 1;
    for (int i = 0; i < n - count; i++) all_odd *= 2;
    cout << total - all_odd << endl;
    
    return 0;
}
