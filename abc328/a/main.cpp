#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, x;
    int sum = 0;
    cin >> n >> x;
    vector<int> s(n);
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i++) {
        if (s[i] <= x) { sum += s[i]; }
    }
    cout << sum << '\n';
}
