n=int(input())
l=[0]*(n+1)
l[0]=1
for i in range(n):
    l[i+1]=sum(sum(map(int,str(l[x]))) for x in range(i+1))
print(l[n])