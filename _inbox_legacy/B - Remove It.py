n, x = map(int, input().split())
a = list(map(int, input().split()))
while x in a:
    a.remove(x)
print(*a)