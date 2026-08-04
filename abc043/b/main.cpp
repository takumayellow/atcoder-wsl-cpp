#include <bits/stdc++.h>
using namespace std;

int main(){
    string s; cin >> s;
    string t;
    for (char c : s) {
        if (c == 'B'){ if (!t.empty()) t.pop_back(); }
        else t.push_back(c);
    }
    cout << t << "\n";
    return 0;
}
