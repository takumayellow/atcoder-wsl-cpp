n, k = map(int, input().split())
s = input()

count = 0  # 食べられた回数
consecutive_o = 0  # 連続する "O" の数

for char in s:
    if char == 'O':
        consecutive_o += 1
    else:
        # 連続 "O" の部分を k ごとにまとめて食べる
        count += consecutive_o // k
        consecutive_o = 0  # 次の連続 "O" にリセット

# 最後の連続部分も処理
count += consecutive_o // k

print(count)
