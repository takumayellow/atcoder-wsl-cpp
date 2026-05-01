n=int(input())
a=list(map(int,input().split()))
s,t=map(list, zip(*[list(map(int, input().split())) for _ in range(n-1)]))
for i in range(n-1):
    while a[i]>=s[i]:
        a[i]-=s[i]
        a[i+1]+=t[i]
print(a[n-1])