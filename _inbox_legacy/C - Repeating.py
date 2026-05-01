n = int(input())
a = list(map(int, input().split()))
b = [-1] * n
last_seen = {}

for i in range(n):
    if a[i] in last_seen:
        b[i] = last_seen[a[i]] + 1  # 1始まりにするため+1
    last_seen[a[i]] = i  # 現在のインデックスを更新

print(*b)