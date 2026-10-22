#include <bits/stdc++.h>
using namespace std;

int main(void) {
    int n, m;
    cin >> n >> m;
    vector<int> a(m, -1);
    for (int i = 0; i < n; i++) {
        int c, s;
        cin >> c >> s;
        c--;
        if (a[c] < s) a[c] = s;
    }
    for (int i = 0; i < m; i++) cout << a[i] << "\n"[i == m-1];
}
