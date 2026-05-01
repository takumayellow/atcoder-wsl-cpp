n = int(input())
s_min = 10**5
for a in range(1, n):  # A は 1 以上
    b = n - a
    s = sum(map(int, str(a))) + sum(map(int, str(b)))
    s_min = min(s_min, s)
print(s_min)
