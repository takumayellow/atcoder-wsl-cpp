#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << (((c < a) || (c == a && d <= b)) ? "Yes" : "No") << "\n";
    return 0;
}
