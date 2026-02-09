#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int A;

    cin >> A;

    if (400%A == 0) cout << 400/A << endl;
    else cout << -1 << endl;
    
    return 0;
}
