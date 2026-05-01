n,m=map(int,input().split())
a=list(map(int,input().split()))
x=list(zip(*[list(map(int, input().split())) for _ in range(n)]))
for i in range(m):
    if sum(x[i])<a[i]:print("No");break
else:print("Yes")