#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int h, b;
    cin >> h >> b;
    cout << max(h-b, 0) << "\n";
    
    return 0;
}
