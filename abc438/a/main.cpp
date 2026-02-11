#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int d, f;
    cin >> d >> f;

    // Day numbers are cyclic in [1, 7].
    int ans = (f - (d % 7) + 6) % 7 + 1;
    printf("%d\n", ans);
    
    return 0;
}
