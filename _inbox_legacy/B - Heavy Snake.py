n, d = map(int, input().split())

# 先にN匹のデータをリストに保存
snakes = [tuple(map(int, input().split())) for _ in range(n)]

# 各 k に対する最大の重さを求める
for k in range(1, d + 1):
    max_weight = 0  # 各 k に対してリセット
    for t, l in snakes:
        weight = t * (l + k)
        max_weight = max(max_weight, weight)
    print(max_weight)
