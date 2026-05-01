n=int(input())
a=list(map(int,input().split()))
c=0

for i in range(2*n-2):
    if a[i+2]==a[i]:c+=1
print(c)