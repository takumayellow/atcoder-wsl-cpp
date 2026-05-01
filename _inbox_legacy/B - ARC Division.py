n,r=map(int,input().split())
t=r
for i in range(n):
    d,a=map(int,input().split())
    if (d==1 and 1600<=t<=2799)or(d==2 and 1200<=t<=2399):t+=a
print(t)