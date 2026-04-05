#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<int> a(N), b(N);
    vector<int> c(M), d(M);
    vector<int> ans(N);

    for (int i = 0; i < N; i++) {
        cin >> a[i] >> b[i];
    }

    for (int i = 0; i < M; i++) {
        cin >> c[i] >> d[i];
    }

    for (int i = 0; i < N; i++) {
        ll best = LLONG_MAX;
        for (int j = 0; j < M; j++) {
            ll dist = abs(a[i] - c[j]) + abs(b[i] - d[j]);
            if (dist < best) {
                best = dist;
                ans[i] = j + 1;  // 1-indexed
            }
        }
    }

    for (int i = 0; i < N; i++) {
        cout << ans[i] << "\n";
    }
    return 0;
}
