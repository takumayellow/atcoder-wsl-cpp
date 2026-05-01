def max_sum(T, test_cases):
    results = []
    
    for n, k, A, B in test_cases:
        # AとBを組み合わせたリストを作成
        combined = sorted(zip(A, B), key=lambda x: (-x[0], x[1]))  # Aの値で降順にソート
        
        # K個の要素を選択して計算
        sum_B = sum(combined[i][1] for i in range(k))  # K個目までのBiの合計
        max_A = combined[k-1][0]  # K個目のAの値を取得
        
        # 指定された式の計算
        max_value = max_A * sum_B
        
        results.append(max_value)
    
    return results

# 入力処理のテスト
T = 3
test_cases = [
    (3, 2, [3, 7, 6], [9, 2, 4]),
    (5, 3, [6, 4, 1, 5, 9], [8, 6, 5, 1, 7]),
    (10, 6, [61, 95, 61, 57, 69, 49, 46, 47, 14, 43], [39, 79, 48, 92, 90, 76, 30, 16, 30, 94])
]

# 結果を出力
results = max_sum(T, test_cases)
print(results)
