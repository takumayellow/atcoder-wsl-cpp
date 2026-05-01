n = int(input())
c = 0
flag = False  # フラグの初期化

for i in range(n):
    d_1, d_2 = map(int, input().split())
    if d_1 == d_2:
        c += 1
        if c == 3:
            flag = True  # 3連続達成時にフラグを立てる
    else:
        c = 0  # 連続が途切れたらリセット

if flag:
    print("Yes")
else:
    print("No")
