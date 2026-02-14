#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<bool>> adjacent(n, vector<bool>(n, false));

    for (int i = 0; i < m; i++) {
        vector<int> x(n);
        for (int j = 0; j < n; j++) {
            cin >> x[j];
            x[j]--;
        }

        for (int j = 0; j + 1 < n; j++) {
            int a = x[j];
            int b = x[j + 1];
            adjacent[a][b] = true;
            adjacent[b][a] = true;
        }
    }

    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (!adjacent[i][j]) {
                ans++;
            }
        }
    }

    cout << ans << '\n';
    return 0;
}
