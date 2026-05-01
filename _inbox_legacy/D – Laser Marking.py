import itertools
import math

# 距離計算関数
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 入力
N, S, T = map(int, input().split())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append((a, b, c, d))

# 初期化
min_time = float('inf')

# すべての順序を試す
for perm in itertools.permutations(A):
    # 始点は(0, 0)
    curr_x, curr_y = 0, 0
    total_time = 0
    
    # 各線分について計算
    for (a, b, c, d) in perm:
        # まず線分の始点に移動 (a, b) か (c, d) に移動し、短い方を選ぶ
        move_to_a = dist(curr_x, curr_y, a, b)
        move_to_b = dist(curr_x, curr_y, c, d)
        
        # より短い距離の方を選んで移動する
        if move_to_a / S < move_to_b / S:
            total_time += move_to_a / S
            curr_x, curr_y = a, b
            total_time += dist(a, b, c, d) / T  # 印字中の移動
            curr_x, curr_y = c, d
        else:
            total_time += move_to_b / S
            curr_x, curr_y = c, d
            total_time += dist(c, d, a, b) / T  # 印字中の移動
            curr_x, curr_y = a, b
    
    # 最小時間を記録
    min_time = min(min_time, total_time)

# 出力 (精度を19桁に設定)
print(f"{min_time:.19f}")
