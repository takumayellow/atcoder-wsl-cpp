n,m=map(int,input().split())
a=list(map(int,input().split()))
f=[False for _ in range(n+1)]
for x in a:f[x]=True
ans=[0 for _ in range(n+1)]
nxt=n
for i in range(n,0,-1):
    if f[i]:
        nxt=i
    ans[i]=nxt-i
print(*ans[1:],sep="\n")