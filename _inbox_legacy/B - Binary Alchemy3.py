# 自然数 N を取得
n = int(input())

# 長方形の部分全体を格納するリスト（0で初期化）
a = [[0] * n for _ in range(n)]

# データの読み込みとリストの更新
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(len(row)):
        a[i][j] = row[j]

i,j=map(int,input().split())
print(a[i][j])