# 自然数 N を取得
n = int(input())

# 長方形の部分全体を格納するリスト（0で初期化）
a = [[0] * n for _ in range(n)]

# データの読み込みとリストの更新
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        a[i][j] = row[j]

# 空の部分に 0 を置く
for i in range(n):
    for j in range(i + 1, n):
        a[i][j] = 0

# 元素 1 から始めて、順に合成する
current_element = 1
for i in range(1, n):
    current_element = a[current_element - 1][i]

# 最終的に得られる元素を出力
print(f"最終的に得られる元素: {current_element}")