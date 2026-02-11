#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    printf("%s\n", n/100==(n/10)%10 && (n/10)%10==n%10 ? "Yes": "No");
    return 0;
}
