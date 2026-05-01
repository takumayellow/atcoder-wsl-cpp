N, Q = map(int, input().split())
instructions = [input().split() for _ in range(Q)]

# 初期位置
left_hand = 1
right_hand = 2
total_moves = 0

for hand, target in instructions:
    target = int(target)

    if hand == 'L':
        # Lの場合、左手を目標にする
        while left_hand != target:
            if (left_hand + 1) % N == right_hand:  # 右手と重なる場合
                # 右手が左手の次にいるので、右手を1つ進める
                right_hand = (right_hand % N) + 1
                total_moves += 1

            # 目標までの移動距離を計算
            dist_clockwise = (target - left_hand) % N
            dist_counterclockwise = (left_hand - target) % N

            # 移動方向を決定
            if dist_clockwise <= dist_counterclockwise:
                # 時計回りに移動
                left_hand = (left_hand % N) + 1
                total_moves += 1
            else:
                # 反時計回りに移動
                left_hand = (left_hand - 1) if left_hand > 1 else N
                total_moves += 1

    elif hand == 'R':
        # Rの場合、右手を目標にする
        while right_hand != target:
            if (right_hand + 1) % N == left_hand:  # 左手と重なる場合
                # 左手が右手の次にいるので、左手を1つ進める
                left_hand = (left_hand % N) + 1
                total_moves += 1

            # 目標までの移動距離を計算
            dist_clockwise = (target - right_hand) % N
            dist_counterclockwise = (right_hand - target) % N

            # 移動方向を決定
            if dist_clockwise <= dist_counterclockwise:
                # 時計回りに移動
                right_hand = (right_hand % N) + 1
                total_moves += 1
            else:
                # 反時計回りに移動
                right_hand = (right_hand - 1) if right_hand > 1 else N
                total_moves += 1

# 結果を出力
print(total_moves)
