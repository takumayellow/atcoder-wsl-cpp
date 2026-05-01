MOD = 998244353

def is_good_integer(n):
    # nの約数の総和を計算する
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
        i += 1
    # 約数の総和が3で割り切れるかチェック
    return total % 3 == 0

def solve(N, M):
    # M 個の整数の総積が N 以下の良い整数になるものの個数を求める
    # dp[x] = 長さxの整数列の総積がN以下の良い整数の個数
    dp = [0] * (N + 1)
    dp[1] = 1  # 1は良い整数として初期化

    for length in range(1, M + 1):
        next_dp = [0] * (N + 1)
        for n in range(1, N + 1):
            if dp[n] > 0:
                for k in range(1, N // n + 1):
                    if is_good_integer(n * k):
                        next_dp[n * k] = (next_dp[n * k] + dp[n]) % MOD
        dp = next_dp

    result = sum(dp) % MOD
    return result

# 入力の受け取り
N, M = map(int, input().split())

# 結果の取得と出力
print(solve(N, M))