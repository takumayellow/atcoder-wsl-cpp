a = list(map(int,input().split()))
c = input()
x = 0 if c=="Red" else 1 if c=="Green" else 2
a.pop(x)
print(min(a))
