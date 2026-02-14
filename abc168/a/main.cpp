#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;

    if (N % 10 == 3) {
        cout << "bon" << endl;
    } else if (N % 10 == 0 || N % 10 == 1 || N % 10 == 6 || N % 10 == 8){
        cout << "pon" << endl;
    } else{
        cout << "hon" << endl;
    }
    return 0;
}
