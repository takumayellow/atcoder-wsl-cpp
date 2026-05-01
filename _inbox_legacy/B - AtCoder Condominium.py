n,k=map(int,input().split())
c=0
for i in range(1,n+1):
    for j in range(1,k+1):
        c+=i*10**2+j
print(c)