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
    # 全ての2つの端点の選び方を試す (1: 始点、2: 終点)
    for case in itertools.product([0, 1], repeat=N):
        # 始点は(0, 0)
        curr_x, curr_y = 0, 0
        total_time = 0

        for idx, (a, b, c, d) in enumerate(perm):
            # case[idx] == 0 のとき (a, b) から (c, d) に移動
            # case[idx] == 1 のとき (c, d) から (a, b) に移動
            if case[idx] == 0:
                move_to_a = dist(curr_x, curr_y, a, b)
                total_time += move_to_a / S
                curr_x, curr_y = a, b
                total_time += dist(a, b, c, d) / T  # 印字中の移動
                curr_x, curr_y = c, d
            else:
                move_to_b = dist(curr_x, curr_y, c, d)
                total_time += move_to_b / S
                curr_x, curr_y = c, d
                total_time += dist(c, d, a, b) / T  # 印字中の移動
                curr_x, curr_y = a, b

        # 最小時間を記録
        min_time = min(min_time, total_time)

# 出力 (精度を19桁に設定)
print(f"{min_time:.19f}")