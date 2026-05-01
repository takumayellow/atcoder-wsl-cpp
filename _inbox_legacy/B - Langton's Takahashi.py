from collections import deque

N = int(input())
S = [input() for _ in range(N)]
INF = 10**9

y1, x1, y2, x2 = -1, -1, -1, -1
for y in range(N):
    for x in range(N):
        if S[y][x] == "P":
            if y1 == -1:
                y1, x1 = y, x
            else:
                y2, x2 = y, x

d = [[[[INF for l in range(N)] for k in range(N)] for j in range(N)] for i in range(N)]
d[y1][x1][y2][x2] = 0
q = deque([(y1, x1, y2, x2)])
ans = -1
while q:
    y1, x1, y2, x2 = q.popleft()
    if y1 == y2 and x1 == x2:
        ans = d[y1][x1][y2][x2]
        break
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny1, nx1 = y1 + dy, x1 + dx
        if not (0 <= ny1 < N and 0 <= nx1 < N and S[ny1][nx1] != "#"):
            ny1, nx1 = y1, x1
        ny2, nx2 = y2 + dy, x2 + dx
        if not (0 <= ny2 < N and 0 <= nx2 < N and S[ny2][nx2] != "#"):
            ny2, nx2 = y2, x2
        if d[ny1][nx1][ny2][nx2] == INF:
            d[ny1][nx1][ny2][nx2] = d[y1][x1][y2][x2] + 1
            q.append((ny1, nx1, ny2, nx2))
print(ans)

