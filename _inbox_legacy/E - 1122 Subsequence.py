# 入力
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:]))

# 要素ごとの出現回数をカウント
count = [0] * 21  # 1 <= A[i] <= 20
for x in A:
    count[x] += 1

# 各要素で使用可能な最大偶数個を計算
max_length = 0
for x in range(1, 21):
    max_length += count[x] // 2 * 2

# 結果を出力
print(max_length)
