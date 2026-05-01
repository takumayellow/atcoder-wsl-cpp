# 入力の取得
N, K = map(int, input().split())
P = [int(x) - 1 for x in input().split()]  # 0インデックスに調整

# 結果を格納するリスト
ans = [0] * N
# すでに処理済みのインデックスを管理するフラグ
used = [False] * N

# 各要素についてサイクルを検出し、そのサイクルでの位置を計算
for i in range(N):
    if not used[i]:
        # iを含むサイクルを求める
        cycle = []
        j = i
        while not used[j]:
            used[j] = True
            cycle.append(j)
            j = P[j]
        # サイクルの長さとシフト量を計算
        cycle_length = len(cycle)
        shift = pow(2, K, cycle_length)  # K回移動後の位置を求める
        
        # サイクル内の位置を更新
        for j in range(cycle_length):
            ans[cycle[j]] = cycle[(j + shift) % cycle_length]
            
# 結果を1インデックスに戻して出力
print(" ".join(str(x + 1) for x in ans))
