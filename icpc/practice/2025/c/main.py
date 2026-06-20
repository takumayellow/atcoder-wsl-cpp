while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = set(map(int, input().split()))
    weekend = 2 * (m // 7) + max(0, m % 7 - 5)          # 6,7 日目が休み
    extra = sum(1 for x in a if 1 <= x <= m and x % 7 not in (6, 0))
    print(m - weekend - extra)
