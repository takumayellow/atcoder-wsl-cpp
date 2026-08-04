#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        g[a].push_back(b);
    }

    vector<bool> seen(n + 1, false);
    queue<int> q;
    q.push(1);
    seen[1] = true;
    int ans = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        ans++;
        for (int v : g[u]) {
            if (!seen[v]) {
                seen[v] = true;
                q.push(v);
            }
        }
    }

    cout << ans << endl;
    return 0;
}
