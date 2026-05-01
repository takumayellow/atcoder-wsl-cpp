n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]

# 各点に対して距離が最大の点を探す
for i in range(n):
    max_distance = -1
    farthest_point = -1
    for j in range(n):
        if i != j:
            # ユークリッド距離の二乗を計算
            distance = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            # 距離が大きいか、同じ距離で番号が小さい場合は更新
            if distance > max_distance or (distance == max_distance and j < farthest_point):
                max_distance = distance
                farthest_point = j
    # 1-indexedなので、+1 して出力
    print(farthest_point + 1)
