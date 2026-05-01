# 解説のコードを書くよ
from bisect import bisect_left, bisect_right

# 入力
N = 4  # 村の数
X = [1, 3, 5, 7]  # 村の座標
P = [1, 2, 3, 4]  # 各村の村人の人数
Q = 4  # クエリの数
queries = [(1, 1), (2, 6), (0, 10), (2, 2)]  # クエリのリスト

# 村人の累積和を計算
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + P[i - 1]

# 各クエリの処理
results = []
for L, R in queries:
    # L以上の最小のインデックスと、R以下の最大のインデックスを見つける
    left = bisect_left(X, L)
    right = bisect_right(X, R) - 1

    if left <= right:
        results.append(prefix_sum[right + 1] - prefix_sum[left])
    else:
        results.append(0)

print(results)  # 結果を出力
