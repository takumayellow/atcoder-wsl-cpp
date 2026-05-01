h, w = map(int, input().split())
si, sj = map(int, input().split())
c = [input() for _ in range(h)]
moves = input()  # 移動指示の文字列を moves に変更
y, x = si - 1, sj - 1  # 座標の初期化

for a in moves:  # ここで moves を使う
    if a == "L" and x > 0 and c[y][x - 1] != "#":
        x -= 1
    if a == "R" and x < w - 1 and c[y][x + 1] != "#":
        x += 1
    if a == "U" and y > 0 and c[y - 1][x] != "#":
        y -= 1
    if a == "D" and y < h - 1 and c[y + 1][x] != "#":
        y += 1

print(y + 1, x + 1)  # 座標を 1-based に戻して出力
