#include <bits/stdc++.h>

using namespace std;

using ll = long long;

ll f(ll n) { return n * (n + 1) / 2; }

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int &i: a) cin >> i;
    ll ans = n;
    int pre = 0;
    for (int i = 1; i < n - 1; i++) {
        if (a[i] - a[i - 1] != a[i + 1] - a[i]) {
            ans += f(i - pre);
            pre = i;
        }
    }
    ans += f(n - 1 - pre);
    cout << ans << endl;
}
