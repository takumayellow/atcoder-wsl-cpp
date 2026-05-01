n,m=map(int,input().split())
a=list(map(int,input().split()))
x=list(zip(*[list(map(int, input().split())) for _ in range(n)]))
for i in range(m):
    x_add=sum(x[i])
    if x_add<a[i]:print("No");break
else:print("Yes")