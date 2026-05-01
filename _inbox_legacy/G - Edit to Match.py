def minimum_edit_cost(n, strings):
    results = []
    
    # 各文字列に対するコストを計算
    for k in range(n):
        target = strings[k]
        min_cost = float('inf')
        
        # 他の文字列と比較してコストを計算
        for j in range(k):
            compare = strings[j]
            # 編集距離の計算
            cost = edit_distance(target, compare)
            min_cost = min(min_cost, cost)
        
        # 自分の文字列を空文字にするコストも考慮
        min_cost = min(min_cost, len(target))  # 空文字にするためのコスト
        
        results.append(min_cost)
    
    return results

def edit_distance(s1, s2):
    len1, len2 = len(s1), len(s2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    for i in range(len1 + 1):
        dp[i][0] = i  # s1を空にするためのコスト
    for j in range(len2 + 1):
        dp[0][j] = j  # s2を空にするためのコスト
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 文字が一致する場合
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,   # 削除
                    dp[i][j - 1] + 1,   # 挿入
                    dp[i - 1][j - 1] + 1 # 置換
                )
    
    return dp[len1][len2]

# 入力処理
N = int(input())
S = [input().strip() for _ in range(N)]

# 結果出力
results = minimum_edit_cost(N, S)
for result in results:
    print(result)
