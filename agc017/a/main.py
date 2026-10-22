n,p = map(int,input().split())
a = list(map(int,input().split()))

c = 0
for i in range(n):
    if a[i]%2 == 1: c = 1

if c ==1:
    print(2**(n-1))
elif p == 0: print(2**n)
else: print(0)

