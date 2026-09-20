# ABC476 C - 素朴解（定義そのまま）。答え合わせ用で、提出はしない。
#
# k ごとに A_1..A_k を丸ごとソートし直すので O(N^2 log N)。
# 小さい N でランダム入力を作り、main.cpp / main.py の出力と突き合わせる用途。

n = int(input())
a = list(map(int, input().split()))

for k in range(3, n + 1):
    b = a[:k]
    c = sorted(b)
    print(c[-3])   # 昇順 c の後ろから 3 番目 = 降順 3 番目
