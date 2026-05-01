n=int(input())
for k in range(n):
    m=sum(i for i in range(k))
    if m>=n:print(k-1);break