n=int(input())
m=10**6
ans=0
for i in range(1,m+1):
    x=i**3
    if x<=n and str(x)==str(x)[::-1]:
        ans=x
print(ans)