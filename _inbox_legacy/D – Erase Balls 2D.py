def count_remaining_sets(N, balls):
    mod = 998244353
    
    remaining_sets = set()

    # すべてのボールを選んで、それに基づく残りのボールを調べる
    for k in range(N):
        remaining = []
        Xk, Yk = balls[k]

        for i in range(N):
            if i == k:
                continue
            
            Xi, Yi = balls[i]
            if (Xi < Xk and Yi < Yk) or (Xi > Xk and Yi > Yk):
                continue  # このボールは削除される
            remaining.append(i)

        # 残ったボールのインデックスをソートしてタプルにする
        remaining_sets.add(tuple(sorted(remaining)))

    # 残ったボールの集合の数を返す
    return len(remaining_sets)

# 入力
N = int(input())
balls = [tuple(map(int, input().split())) for _ in range(N)]

# 出力
print(count_remaining_sets(N, balls) % 998244353)
