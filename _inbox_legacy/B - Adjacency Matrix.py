n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result = []
    for j in range(n):
        if a[i][j] == 1:
            result.append(str(j + 1))  # j + 1で頂点番号に変換
    print(" ".join(result))  # joinでリストの要素を結合して出力
