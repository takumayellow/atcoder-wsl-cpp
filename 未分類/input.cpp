#include <iostream>
#include <vector> // ← これが必要！
using namespace std;

int main(){
    int N;
    cin >> N;

    vector<int> data(N);
    for (int i = 0; i < N; i++) {
        cin >> data[i]; // ← セミコロン忘れずに！
    }

    for (int i = 0; i < 3; i++) {
        data.push_back(i);
    }

    data.pop_back();

    for (int i = 0; i < N + 2; i++) {
        cout << data[i] << " "; // 改行はなくてもいいけど見やすくね！
    }

    cout << endl; // 最後に改行もつけとこ！
    return 0;
}
