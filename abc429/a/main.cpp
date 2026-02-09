#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    int ok_count = min(n, m);
    for (int i = 0; i < ok_count; i++) {
        cout << "OK\n";
    }

    for (int i = ok_count; i < n; i++) {
        cout << "Too Many Requests\n";
    }

    return 0;
}
