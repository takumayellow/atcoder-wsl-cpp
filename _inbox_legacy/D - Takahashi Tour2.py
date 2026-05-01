import sys
sys.setrecursionlimit(10**6)
n=int(input())
connect=[[]for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)
for i in range(n+1):
    connect[i].sort()
ans=[]
def dfs(now,pre):
    ans.append(now)
    for to in connect[now]:
        if to!=pre:
            dfs(to,now)
            ans.append(now)
dfs(1,-1)
print(*ans)