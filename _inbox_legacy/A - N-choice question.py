n, a, b = map(int, input().split())
c = list(map(int, input().split()))
p = a + b

for i in range(n):
    if c[i] == p:
        print(i+1)
        break  # 見つかったらループを終了