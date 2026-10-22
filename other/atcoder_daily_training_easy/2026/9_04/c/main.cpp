#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
    string n;
    cin >> n;

    vector<int> N(n.size());
    for (int i = 0; i < n.size(); i++) {
        N[i] = n[i] - '0';
        cout << N[i] << endl;
    }
}
