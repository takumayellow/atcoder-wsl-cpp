N, M, K = map(int, input().split())
A = list(map(int, input().split()))

# すべての票の合計
used_votes = sum(A)
remaining_votes = K - used_votes

# 結果を格納するリスト
result = []

# 各候補者について、必要な票数を計算
for i in range(N):
    # 現在の候補者 A[i] について、A[i] より票が多い候補者の数をカウント
    count_more = sum(1 for x in A if x > A[i])
    
    # count_more が M 以上なら、この候補者は当選する可能性がない
    if count_more < M:
        result.append(0)  # すでに当選確定している
    else:
        # 必要な追加票数を計算する
        additional_votes_needed = max(0, max(A) - A[i] + 1)
        
        # 残り票数で間に合うかどうかを確認
        if additional_votes_needed <= remaining_votes:
            result.append(additional_votes_needed)
        else:
            result.append(-1)

# 結果を出力
print(" ".join(map(str, result)))
