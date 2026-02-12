#include<bits/stdc++.h>

using namespace std;

int main(){
    vector<int> a(3);
    cin >> a[0] >> a[1] >> a[2];
    sort(a.begin(),a.end());
    do{
        if (a[0]*a[1] == a[2]){cout << "Yes\n"; return 0;}
    }while(next_permutation(a.begin(),a.end()));
    cout << "No\n";
    return 0;
}