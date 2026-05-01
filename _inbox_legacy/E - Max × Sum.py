def min_value_for_k_subset(T, test_cases):
    results = []
    for n, k, A, B in test_cases:
        # Aのインデックスを保持したペアを作成
        pairs = [(A[i], B[i]) for i in range(n)]
        
        # Aを降順にソートし、対応するBを取得
        pairs.sort(reverse=True, key=lambda x: x[0])  # Aの値でソート
        max_a = pairs[k - 1][0]  # k番目の最大値
        sum_b = sum(p[1] for p in pairs[:k])  # k個のBの合計
        
        # 計算結果
        result = max_a * sum_b
        results.append(result)
    
    return results

# 入力の受け取り
import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
test_cases = []

line_index = 1
for _ in range(T):
    n, k = map(int, data[line_index].split())
    line_index += 1
    A = list(map(int, data[line_index].split()))
    line_index += 1
    B = list(map(int, data[line_index].split()))
    line_index += 1
    test_cases.append((n, k, A, B))

# 結果を計算
results = min_value_for_k_subset(T, test_cases)

# 結果を出力
print('\n'.join(map(str, results)))
