N, M = map(int, input().split())
A = list(map(int, input().split()))

# prefix_sumを使って累積和を計算
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + A[i - 1]) % M

total_sum = 0

# lを固定してrを動かす
for l in range(1, N + 1):
    for r in range(l, N + 1):
        subarray_sum = (prefix_sum[r] - prefix_sum[l - 1]) % M
        total_sum += subarray_sum

print(total_sum)
