n=int(input())
a=list(map(int,input().split()))
c,ans=[0 for _ in range(n+1)],[]
for x in a:
    c[x]+=1
    if c[x]==2:
        ans.append(x)
print(" ".join(map(str,ans)))