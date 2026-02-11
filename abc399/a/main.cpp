#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    string s, t;
    cin >> n >> s >> t;

    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] != t[i]) ans++;
    }
    printf("%d\n", ans);
    
    return 0;
}
