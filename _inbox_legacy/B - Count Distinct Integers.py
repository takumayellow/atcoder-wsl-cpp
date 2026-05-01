n=int(input())
a=list(map(int,input().split()))
c=0
l=[]
for i in range(n):
    if a[i]not in l:
        c+=1
        l.append(a[i])
print(c)