def count_mountain_folds(N, A):
    max_val = 0

    # 再帰的に山折りと谷折りを生成する関数
    def fold_pattern(level):
        if level == 0:
            return ['V']
        else:
            prev = fold_pattern(level - 1)
            return prev + ['V'] + ['M' if i == 'V' else 'V' for i in prev]

    # 100回折りたたんだ結果を再帰で取得
    pattern = fold_pattern(100)
    
    # f(i) の最大値を計算する
    for i in range(2**100 - A[-1] - 1):
        count = sum(1 for a in A if pattern[i + a] == 'M')
        max_val = max(max_val, count)

    return max_val

# 入力の処理
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
result = count_mountain_folds(N, A)
print(result)