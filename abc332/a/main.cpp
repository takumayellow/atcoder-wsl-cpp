#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,s,k;
    cin >> n >> s >> k;
    int sum = 0;

    for (int i = 0; i < n; i++) {
        int p,q;
        cin >> p >> q;
        sum += p * q;
    }
    
    sum += (sum < s ? k : 0);

    cout << sum << endl;
    return 0;
}
