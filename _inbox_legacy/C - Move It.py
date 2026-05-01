n=int(input())
a=list(map(int,input().split()))
w=list(map(int,input().split()))
b=[0]*(n+1)
for i in range(n):
    b[a[i]]=max(b[a[i]],w[i])
print(sum(w)-sum(b))