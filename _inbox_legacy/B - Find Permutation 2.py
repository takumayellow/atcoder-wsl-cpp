n=int(input())
a=list(map(int,input().split()))
p=[0]*(n)
l0=[x for x in range(1,n+1)]
l0.append(-1)
l=list(set(l0) - set(a))
print(l)

c=0

for i in range(n):
    if a[i]!=-1:p[i]="inf"
    if a[i]==-1:
        p[i]=l[c];c+=1
    print(p)
print("Yes")
print(*p)

# if a[i] in p:print("No");break
#         else: p[i]=a[i]