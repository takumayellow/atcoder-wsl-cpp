n=int(input())
a,b=map(list, zip(*[list(map(int, input().split())) for _ in range(n)]))
print(a,b)