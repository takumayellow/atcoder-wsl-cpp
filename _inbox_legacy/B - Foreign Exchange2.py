n = int(input())
a = list(map(int, input().split()))
s = []
t = []

for _ in range(n - 1):
    si, ti = map(int, input().split())
    s.append(si)
    t.append(ti)

for i in range(n - 1):
    while a[i] >= s[i]:
        a[i] -= s[i]
        a[i + 1] += t[i]

print(a[n - 1])
