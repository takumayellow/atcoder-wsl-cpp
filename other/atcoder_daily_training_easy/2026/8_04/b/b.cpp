#include<bits/stdc++.h>
using namespace std;

int main(void) {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);

    for(int i = 0; i < n; i++) cin >> a[i];

    bool ok = true;
    for (int i = 0; i < n; i++) { 
        if (a[i] > m) { ok = false; break;}
    }
    cout << (ok ? "Yes": "No") << endl;
}



