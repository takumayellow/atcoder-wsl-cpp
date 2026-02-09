#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int x, y;
    cin >> x >> y;
    int sum = x + y;
    cout << (sum % 12 == 0 ? 12 : sum % 12) << "\n";    
    return 0;
}
