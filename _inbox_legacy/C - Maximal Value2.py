n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if i==0:
        ans+=a[0]
    elif i==n-1:
        ans+=a[-1]
    else:
        ans+=min(a[i-1],a[i])
print(ans)