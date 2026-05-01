#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    long long sum = 0;
    for (int i = 0; i < N; ++i) {
        int a;
        cin >> a;
        sum += a;
    }

    cout << sum << "\n";
    return 0;
}
