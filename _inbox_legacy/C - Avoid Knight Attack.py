def count_safe_cells(N, M, positions):
    # 駒の動きの方向を定義
    knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                    (-2, -1), (-1, -2), (1, -2), (2, -1)]
    
    # 駒の位置を管理するセットと、攻撃されるセルを記録するセットを作成
    attacked_positions = set()
    knight_positions = set(positions)

    # 駒ごとに攻撃されるセルを計算し、管理するセットに追加
    for x, y in knight_positions:
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            # 有効範囲内にある場合のみ追加
            if 1 <= nx <= N and 1 <= ny <= N:
                attacked_positions.add((nx, ny))
    
    # 全セル数 - 攻撃範囲セル数 - 駒セル数
    total_cells = N * N
    attacked_or_knight_cells = len(attacked_positions | knight_positions)  # 両方のセットを合計
    safe_cells = total_cells - attacked_or_knight_cells

    return safe_cells

# 入力の処理
N, M = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(M)]

# 結果を出力
print(count_safe_cells(N, M, positions))
