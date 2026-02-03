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

    int pad = n - (int)s.length();
    if (pad < 0) pad = 0;
    for (int i = 0; i < pad; i++) putchar('o');
    printf("%s\n", s.c_str());
    
    return 0;
}
