n, m = 9, 3
# 9行9列の入力を受け取る
a = [list(map(int, input().split())) for _ in range(n)]

# 各行、各列、各3x3のブロックを管理するためのセット
row = [set() for _ in range(n)]
col = [set() for _ in range(n)]
blo = [[set() for _ in range(m)] for _ in range(m)]

# 各マスについて、行、列、3x3のブロックに数字を追加
for i in range(n):
    for j in range(n):
        # 現在のマスの数字
        num = a[i][j]
        # 行、列、3x3ブロックに数字を追加
        row[i].add(num)
        col[j].add(num)
        blo[i // m][j // m].add(num)

# 条件を満たすかどうか確認
if (
    all(len(r) == 9 for r in row) and  # 各行に1〜9の数字が1つずつある
    all(len(c) == 9 for c in col) and  # 各列に1〜9の数字が1つずつある
    all(all(len(b) == 9 for b in br) for br in blo)  # 各3x3のブロックに1〜9の数字が1つずつある
):
    print("Yes")
else:
    print("No")