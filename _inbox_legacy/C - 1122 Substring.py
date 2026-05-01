n = int(input())
s = input()

# `/` の位置を探す
slashes = [i for i, char in enumerate(s) if char == '/']

max_length = 0

# 各 `/` を中心に 11/22 文字列を探す
for center in slashes:
    # 左側に伸ばして `1` の数を数える
    left_count = 0
    for i in range(center - 1, -1, -1):
        if s[i] == '1':
            left_count += 1
        else:
            break

    # 右側に伸ばして `2` の数を数える
    right_count = 0
    for i in range(center + 1, n):
        if s[i] == '2':
            right_count += 1
        else:
            break

    # 条件を満たす部分文字列の長さを計算
    current_length = 1 + 2 * min(left_count, right_count)
    max_length = max(max_length, current_length)

# 結果を出力
print(max_length)
