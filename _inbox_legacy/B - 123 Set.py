import math

def min_operations(N):
    # このアプローチでは N の平方根までで因数分解することがポイントだよ
    sqrt_n = int(math.sqrt(N))  # Nの平方根まで調べる
    operations = 0

    # xの可能な最小の値は sqrt(N) の倍数まで見る
    for x in range(1, sqrt_n + 1):
        if N % x == 0:  # Nがxで割り切れるなら
            # xとN//xを使って操作をカバーできる
            operations += 1
    return operations

# 入力を受け取る
N = int(input())
print(min_operations(N))