#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string s;
    cin >> s;

    int n = s.count('N');
    int w = s.count('W');
    int s = s.count('S');
    int e = s.count('E');

    if (n % 2 == w % 2 && w % 2 == s % 2) {
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }    
    return 0;
}
