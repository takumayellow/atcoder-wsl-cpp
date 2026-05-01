n = int(input())  # 入力された行数を取得

# 行列の入力をリストとして取得（文字列として）
a = [input().strip() for _ in range(n)]
b = [input().strip() for _ in range(n)]

# 行列を比較して異なる位置を出力
for i in range(n):
    for j in range(len(a[i])):  # 各行の長さでループする
        if a[i][j] != b[i][j]:
            print(i + 1, j + 1)