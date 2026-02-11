#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int a,b,d;
    cin >> a >> b >> d;
    bool first = true;
    for (int x = a; x <= b; x += d){
        if (!first) cout << ' ';
        cout << x;
        first = false;
    }
    cout << '\n';
    return 0;
}
