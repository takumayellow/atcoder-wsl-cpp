n,x=map(int,input().split())
p=list(map(int,input().split()))
s=sum([p[i] for i in range(n)])
print(x/s)