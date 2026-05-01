N,P=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(N):
    if l[i]<P: count=count+1
print(count)