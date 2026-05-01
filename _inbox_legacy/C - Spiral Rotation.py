n = int(input())  # グリッドのサイズ
a = [list(input()) for _ in range(n)]  # グリッドを入力として受け取る

# スパイラル回転を n // 2 回行う
grids = [a]  # 初期のグリッドをリストに追加

# n // 2 回の更新を行う
for _ in range(n // 2):
    new_grid = [[''] * n for _ in range(n)]  # 新しいグリッドを初期化
    
    # 外側から内側へ進む
    for i in range(n // 2):  # i は 0 から n//2 - 1 まで
        for x in range(i, n - i):  # xの範囲をi以上N-i以下でループ
            for y in range(i, n - i):  # yの範囲をi以上N-i以下でループ
                new_x = y  # 新しいx位置
                new_y = n - 1 - x  # 新しいy位置

                new_grid[new_x][new_y] = grids[-1][x][y]  # マスの色を交換

    grids.append(new_grid)  # 新しいグリッドをリストに追加

# 最後のグリッドを出力する
for row in grids[-1]:
    print("".join(row))
