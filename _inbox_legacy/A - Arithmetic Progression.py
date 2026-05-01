a, b, d = map(int, input().split())
l = [a]
while l[-1] + d <= b:
    l.append(l[-1] + d)
print(' '.join(map(str, l)))