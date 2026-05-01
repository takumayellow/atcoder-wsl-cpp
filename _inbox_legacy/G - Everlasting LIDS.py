N, M = map(int, input().split())
A = list(map(int, input().split()))

# prefix_sumを使って累積和を計算
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

# 合計を計算
total_sum = 0
for l in range(1, N + 1):
    for r in range(l, N + 1):
        # 部分配列の和を計算
        subarray_sum = prefix_sum[r] - prefix_sum[l - 1]
        total_sum += subarray_sum % M

print(total_sum)
