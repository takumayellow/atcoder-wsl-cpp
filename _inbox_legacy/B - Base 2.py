a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    c+=a[i]*2**i
print(c)