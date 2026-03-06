#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    ll ans = 0;
    for (int x = 1; x <= N; ++x) {
        for (int y = 1; y <= N; ++y) {
            int z = K - x - y;
            if (1 <= z && z <= N) {
                ++ans;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
