def avoid_queen_attack(n, m, positions):
    attacked_rows = set()
    attacked_cols = set()
    attacked_diag1 = set()  # i + j
    attacked_diag2 = set()  # i - j

    for ak, bk in positions:
        attacked_rows.add(ak)
        attacked_cols.add(bk)
        attacked_diag1.add(ak + bk)
        attacked_diag2.add(ak - bk)

    # 攻撃されるマスの数を計算
    attacked_count = 0

    # 攻撃されている行の数
    attacked_count += len(attacked_rows) * n
    # 攻撃されている列の数
    attacked_count += len(attacked_cols) * n

    # 行と列の交差部分を引く
    attacked_count -= len(attacked_rows) * len(attacked_cols)

    # 対角線の影響を計算
    # それぞれの攻撃対象の対角線に対して
    for ak, bk in positions:
        # i + j = ak + bk の場合の影響
        diag1 = ak + bk
        if 1 <= diag1 <= 2 * n:
            if diag1 <= n + 1:
                attacked_count += diag1 - 1  # 1からdiag1-1まで
            else:
                attacked_count += (2 * n - diag1 + 1)  # diag1からnまで

        # i - j = ak - bk の場合の影響
        diag2 = ak - bk
        if -n + 1 <= diag2 <= n - 1:
            if diag2 < 0:
                attacked_count += n + diag2  # 1からn+diag2まで
            else:
                attacked_count += n - diag2  # diag2からnまで

    # 自分の駒を置ける空マスの個数を計算
    total_cells = n * n
    free_cells = total_cells - attacked_count

    return free_cells

# 入力処理
N, M = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(M)]

# 出力
result = avoid_queen_attack(N, M, positions)
print(result)
