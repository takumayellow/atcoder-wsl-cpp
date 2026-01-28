#include <bits/stdc++.h>
using namespace std;

// x と y の値を交換する関数（ただし値渡し）
void swap_val(int x, int y) {
    int temp = x;
    x = y;
    y = temp;

    // この関数内部では確かに入れ替わっている
    cout << x << " " << y << endl; // → 10 5

    return; // しかし値渡しなので…
}

int main() {
    int x = 5, y = 10;
    swap_val(x, y);    // swap_val 内では 10 5 が出力される

    // main では元の x,y は入れ替わらない
    cout << x << " " << y << endl; // → 5 10

    return 0;
}
