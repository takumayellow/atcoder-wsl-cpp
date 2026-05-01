n=int(input())
a=list(map(int,input().split()))
l0=[x for x in range(1,n+1)]
p=list(a)
p.remove(-1)
print(p)
if p!=list(set(p)):print("No");exit()
res=list(set(l0)-set(p))
index_inv=[i for i, x in enumerate(a) if x==-1]
for i in range(len(index_inv)):
    a[index_inv[i]]=res[-1];res.pop()
print("Yes")
print(*a)