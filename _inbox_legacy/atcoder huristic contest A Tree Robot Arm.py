def main():
    # 入力の読み込み
    N, M, V = map(int, input().split())
    initial_grid = [list(map(int, list(input().strip()))) for _ in range(N)]
    target_grid = [list(map(int, list(input().strip()))) for _ in range(N)]

    # ロボットアームの設計
    vertices = V
    parent = [-1] * vertices  # 親のリスト
    lengths = [1] * (vertices - 1)  # 各辺の長さを1に設定

    # 親をバイナリツリーのように設定
    for i in range(1, vertices):
        parent[i] = (i - 1) // 2  # 親を設定

    # 初期位置を固定
    root_x, root_y = 0, 0

    # 出力
    print(vertices)
    for i in range(1, vertices):
        print(parent[i], lengths[i - 1])
    print(root_x, root_y)

    # 初期位置の設定
    current_x, current_y = root_x, root_y
    holding = False  # たこ焼きを持っているかどうか

    # 操作列の生成
    operations = []

    # たこ焼きを持つための移動
    while not holding:
        if current_y + 1 < N and initial_grid[current_x][current_y + 1] == 1:  # 右にたこ焼きがある場合
            operations.append("R")  # 右に移動
            current_y += 1
            operations.append("P")  # 掴む
            holding = True
            initial_grid[current_x][current_y] = 0  # 掴む
        elif current_y + 1 < N:  # 右に移動できる場合
            operations.append("R")  # 右に移動
            current_y += 1
        else:
            break  # 右に移動できない場合はループを終了

    # たこ焼きを持っている場合の動き
    if holding:
        # 下に移動してたこ焼きを置く
        if current_x + 1 < N:
            operations.append("D")  # 下に移動
            current_x += 1
            operations.append("P")  # 離す
            holding = False
            initial_grid[current_x][current_y] = 1  # 離す

    # 出力
    for op in operations:
        print(f"Current Position: ({current_x}, {current_y}), Holding: {holding}")

        # 各操作を個別に実行
        for command in op:
            print(f"Executing command: {command}")  # 実行するコマンドを表示
            if command == 'R':
                if current_y + 1 < N:  # 範囲をチェック
                    current_y += 1
            elif command == 'L':
                if current_y - 1 >= 0:  # 範囲をチェック
                    current_y -= 1
            elif command == 'U':
                if current_x - 1 >= 0:  # 範囲をチェック
                    current_x -= 1
            elif command == 'D':
                if current_x + 1 < N:  # 範囲をチェック
                    current_x += 1
            elif command == 'P':
                # たこ焼きを持つロジック
                if initial_grid[current_x][current_y] == 0 and not holding:
                    holding = True  # 掴む
                    initial_grid[current_x][current_y] = 1  # 状態更新
                    print(f"Picked up takoyaki at ({current_x}, {current_y})")
                elif initial_grid[current_x][current_y] == 1 and holding:
                    holding = False  # 離す
                    initial_grid[current_x][current_y] = 0  # 状態更新
                    print(f"Dropped takoyaki at ({current_x}, {current_y})")

        # ここで位置を更新するように
        print(f"Position after operation: ({current_x}, {current_y}), Holding: {holding}")

if __name__ == "__main__":
    main()
