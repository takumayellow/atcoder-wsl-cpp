n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for j in range(m):
    for i in range(n):
        if a[i]<=b[j]:print(i+1);break
    else:print(-1)