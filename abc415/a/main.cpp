#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, x;
    int a[100];

    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    cin >> x;
    
    printf("%s\n", find(a, a + n, x) != a + n ? "Yes" : "No");
    
    return 0;
}
