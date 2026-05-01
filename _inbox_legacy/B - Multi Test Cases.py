t = int(input())
l = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for j in range(n):
        if a[j] % 2 == 1:
            c += 1
    l.append(c)

# 各要素を改行しながら出力
print("\n".join(map(str, l)))