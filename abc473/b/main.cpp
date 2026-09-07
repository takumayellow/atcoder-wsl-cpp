#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {

    int n;
    cin >> n;
    vector<int> data(n);

    map<int, int> card;
    
    for (int i = 0; i < n; i++) {
        cin >> data.at(i);
    }

    for (int i = 0; i < n; i++) {
        card[data.at(i)] += 1; 
    }

    int sum = 0;
    
    for (int i = 0; i <= 101; i++) {
        sum += i * (card[i]%2);
    }

    cout << sum << endl;

    return 0;
}
