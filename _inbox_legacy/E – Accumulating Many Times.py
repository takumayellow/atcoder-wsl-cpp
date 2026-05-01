def accumulate_sequences(N, M, sequences):
    final_states = [[0] * M for _ in range(N)]

    for i in range(N):
        current_sum = 0
        for k in range(M):
            current_sum += sequences[i][k]
            final_states[i][k] = current_sum % 2

    total_sum = 0
    MOD = 998244353

    for i in range(N):
        for j in range(N):
            if i != j:
                count = 0
                # 各要素を比較して異なるところをカウント
                for k in range(M):
                    if final_states[i][k] != final_states[j][k]:
                        count += 1
                total_sum = (total_sum + count) % MOD

    return total_sum

# 入力
N, M = map(int, input().split())
sequences = [list(map(int, input().split())) for _ in range(N)]

# 出力
print(accumulate_sequences(N, M, sequences))
