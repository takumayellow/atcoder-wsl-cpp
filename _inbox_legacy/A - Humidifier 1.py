n=int(input())
t,v=map(list, zip(*[list(map(int, input().split())) for _ in range(n)]))
l=v[0]
for i in range(1,n):
    if l>t[i]-t[i-1]:l-=t[i]-t[i-1]
    else:l=0
    l+=v[i]
print(l)
