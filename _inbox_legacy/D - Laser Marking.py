import itertools
import math

# 距離計算関数
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 入力
N, S, T = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

# 初期化
min_time = float('inf')

# すべての順序を試す
for perm in itertools.permutations(A):
    # 各順序に対して2つの端点の選び方をbit全探索
    for i in range(1 << N):
        total_time = 0.0
        curr_x, curr_y = 0, 0
        
        # 各線分について計算
        for j, (a, b, c, d) in enumerate(perm):
            if i & (1 << j):  # bitが1の場合：始点から終点
                total_time += dist(curr_x, curr_y, a, b) / S  # 現在位置から始点まで移動
                total_time += dist(a, b, c, d) / T  # 始点から終点まで印字
                curr_x, curr_y = c, d  # 現在位置を終点に更新
            else:  # bitが0の場合：終点から始点
                total_time += dist(curr_x, curr_y, c, d) / S  # 現在位置から終点まで移動
                total_time += dist(c, d, a, b) / T  # 終点から始点まで印字
                curr_x, curr_y = a, b  # 現在位置を始点に更新
        
        # 最小時間を記録
        min_time = min(min_time, total_time)

# 結果を出力 (精度を12桁に設定)
print(f"{min_time:.12f}")