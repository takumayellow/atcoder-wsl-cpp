#include <atcoder/all>
#include <iostream>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    ll N;
    cin >> N;
    cout << (1LL << N) - 2LL * N << "\n";

    return 0;
}
