#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> c(n), s(n);
    rep(i,n) cin >> c[i] >> s[i];

    for (int i = 1; i <= m; i++) {
        int ans = -1;
        rep(j,n) {
            if (c[j] == i) ans = max(ans, s[j]);
        }
        cout << ans << ' ';
    }
    cout << endl;
    return 0;
}
