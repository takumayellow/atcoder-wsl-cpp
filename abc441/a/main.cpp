#include<stdio.h>
#include<iostream>
using namespace std;
int main(){
    int p,q;
    int x,y;
    cin >> p >> q;
    cin >> x >> y;
    if (p<= x && x <= p+99 && q <= y && y <= q+99){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}