MOD = 998244353

def mod_inv(x, mod=MOD):
    # 逆元の計算（フェルマーの小定理）
    return pow(x, mod - 2, mod)

def treasure_hunt_expectations(T, test_cases):
    results = []
    
    for N, parents, weights in test_cases:
        # 木構造の構築
        tree = [[] for _ in range(N + 1)]
        for i in range(1, N + 1):
            tree[parents[i - 1]].append(i)
        
        # 重みの合計
        total_weight = sum(weights) % MOD
        inv_total_weight = mod_inv(total_weight)
        
        # 各頂点の期待値
        dp = [0] * (N + 1)
        
        def dfs(node):
            result = 0
            for child in tree[node]:
                dfs(child)
                result += dp[child]
                result %= MOD
            if node != 0:  # 根でないなら、その重みに応じた期待値を計算
                dp[node] = (result * mod_inv(weights[node - 1])) % MOD
                dp[node] = (dp[node] + 1) % MOD
        
        # DFS 開始
        dfs(0)
        
        # 根の期待値から期待操作回数を導出
        expected_moves = (dp[0] * total_weight) % MOD
        results.append(expected_moves)
    
    return results

# 入力処理
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    parents = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    test_cases.append((N, parents, weights))

# 各テストケースの結果を出力
results = treasure_hunt_expectations(T, test_cases)
print("\n".join(map(str, results)))
