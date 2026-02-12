#include<bits/stdc++.h>
using namespace std;

bool solve(){
    int a, b, c;
    cin >> a >> b >> c;
    if (a*b == c) return true;
    if (a*c == b) return true;
    if (b*c == a) return true;
    return false;
}

int main(){
    if (solve()) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}