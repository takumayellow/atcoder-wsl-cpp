N=int(input())
l=list(map(int,input().split()))
c=0
for i in range(N):
    if l[i]>=10: c=c+(l[i]-10)
print(c)