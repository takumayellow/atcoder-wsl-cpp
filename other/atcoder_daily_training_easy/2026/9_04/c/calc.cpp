#include <iostream>
#include <string>
#include <vector>
using namespace std;

int digit_sum(int x) {
    int s = 0;
    while (x > 0) {
        s += x % 10;
        x /= 10;
    }
    return s;
}

int main(void) {
    int n;
    cin >> n;

    int a = 1;
    int s = 0;
    for (int i = 0; i < n; i++) {
        s += digit_sum(a);
        a = s;
    }
    cout << a << endl;
}
