#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
    int n;
    string s;
    char c_1, c_2;
    cin >> n >> c_1 >> c_2 >> s;
    for (int i = 0; i < n; i++){
        if (s[i] != c_1){
            cout << c_2;
        }else cout << s[i];
    }
    cout << endl;
}