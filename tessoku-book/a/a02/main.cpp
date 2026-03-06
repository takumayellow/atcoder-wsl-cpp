/*#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, X;
    int A;
    int cnt = 0;

    cin >> N >> X;
    for(int i = 0; i < N; i++){
        cin >> A;
        if(A == X){
            cnt++;
        }
    }
    if(cnt > 0){
        cout << "Yes" << endl;
    }
    else if(cnt == 0){
        cout << "No" << endl;
    }
    return 0;
}
*/
#include <iostream>
using namespace std;

int N, X, A[109];
bool Answer = false;

int main(){
    cin >> N >> X;
    for(int i = 1; i <= N; i++){
        cin >> A[i];
    }
    for(int i = 1; i <= N; i++){
        if(A[i] == X){
            Answer = true;
        }

    }
    if(Answer == true){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
    return 0;
}