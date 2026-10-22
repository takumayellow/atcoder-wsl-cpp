import sys
input = sys.stdin.readline

n, q = map(int,input().split())
p = list(map(int, input().split()))

nxt = [0] * (n + 1)
prv = [0] * (n + 1)

prev = 0
for v in P:
    nxt[prev] = v
    prv[v] = prev
    prev = v
nxt[prev] = 0
prv[0] = prev

for _ in range(q):
    x = int(input())
    if prv[0] == x:
        continue
    a, b = prv[x], nxt[x]
    nxt[a] = b
    prv[b] = a
    t = prv[0]
    nxt[t]=x
    prv[x]=t
    nxt[x]=0
    prv[0]=x

res, v = [], nxt[0]
while v:
    res.append(v)
    v = nxt[v]
print(*res)

