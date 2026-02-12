#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, l, r;
    cin >> n >> l >> r;
    int count = 0;
    for (int i = 1; i <= n; i++){
        int x, y;
        cin >> x >> y;
        if (x <= l && r <= y){
            count ++;
        }
    }
    
    cout << count << "\n";
    return 0;
}
