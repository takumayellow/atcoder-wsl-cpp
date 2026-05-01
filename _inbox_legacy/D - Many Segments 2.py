def count_non_inclusive_segments(N, M, intervals):
    # 各座標に含まれる区間を記録するカウンタを用意
    covered = [0] * (M + 2)

    # 各区間 [L_i, R_i] のカバー範囲を記録
    for L, R in intervals:
        covered[L] += 1
        if R + 1 <= M:
            covered[R + 1] -= 1

    # カバー範囲を累積和で計算（各マスが何回カバーされているかを記録）
    for i in range(1, M + 1):
        covered[i] += covered[i - 1]

    # 条件を満たす範囲を数える
    result = 0
    l = 1
    for r in range(1, M + 1):
        # [l, r] の範囲が条件を満たすまで l を移動
        while l <= r and covered[r] - covered[l - 1] == r - l + 1:
            l += 1
        # 現在の r で有効な l の数を追加
        result += r - l + 1
    
    return result

# 入力の処理
N, M = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# 結果を出力
print(count_non_inclusive_segments(N, M, intervals))
