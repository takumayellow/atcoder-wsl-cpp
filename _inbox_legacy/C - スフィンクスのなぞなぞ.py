n, m = map(int, input().split())
if n * 2 <= m <= n * 4:
    t = n * 4 - m
    q = t % 2
    r = t // 2
    if q == 0:
        print(r, 0, n - r)
    else:
        print(r, 1, n - r - 1)
else:
    print(-1, -1, -1)