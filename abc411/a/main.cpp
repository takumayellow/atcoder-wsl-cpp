#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string p;
    int l;
    cin >> p >> l;

    printf("%s\n", static_cast<int>(p.length()) >= l ? "Yes" : "No");
    
    return 0;
}
