/*#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int pow(int a, int b);
int pow(int a, int b){
    int res = 1;
    for(int i = 0; i < b; i++){
        res *= a;
    }
    return res;
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;
    for(int i = 9; i >= 0; i--){
        int tmp = N;
        tmp = tmp / pow(2, i);
        tmp = tmp % 2;
        cout << tmp;
    }
    cout << "\n";
    return 0;
}
*/
#include <iostream>
using namespace std;
int main(){
    int N;
    cin >> N;
    for(int i = 9; i >= 0; --i){
        cout << ((N >> i) &1);
    }
    cout << "\n";
    return 0;
}