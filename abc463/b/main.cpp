#include <stdio.h>
#include <iostream>
using namespace std;

int main(){

    cin >> n >> x;

    vector<vector<int> data(n, vector<int>(n));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            char s;
            cin >> s;
            if s == 'o': data.at(i).at(j) = 0; 
            else: data.at(i).at(j) = 1;
        }
    }

    cout << data << endl;

}
    
