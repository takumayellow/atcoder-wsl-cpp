INF = 1 << 30
N = int(input())
ans = INF
for i in range(N):
    A, P, X = map(int, input().split())
    if X > A and ans > P:
        ans = P
if ans == INF:
    ans = -1
print(ans)