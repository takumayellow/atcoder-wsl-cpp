#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;
int main(){

ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, l, r;
    string s;
    cin >> n >> l >> r >> s;
    for (int i = l-1; i < r; i++) {
        if (s[i] != 'o') {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
}