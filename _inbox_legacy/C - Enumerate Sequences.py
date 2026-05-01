from itertools import product

n, k = map(int, input().split())
r = list(map(int, input().split()))

for a in product(*(range(1,x+1) for x in r)):
    if not sum(a) % k:
        print(*a)