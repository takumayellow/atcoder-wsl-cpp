#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    string s;
    cin >> n >> s;
    printf("%s\n", s.substr(s.size() >=3 ? s.size()-3 : 0) == "tea" ? "Yes" : "No");
    return 0;
}
