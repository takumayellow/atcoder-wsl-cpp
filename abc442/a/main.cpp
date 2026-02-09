#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s; int sum = 0;
    cin >> s;
for (int i = 0; i < s.size(); i++) {
        if (s[i] == 'i' || s[i] == 'j') {
            sum++;
        }
    }
    cout << sum << "\n";
    return 0;
}
