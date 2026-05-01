n=int(input())
a=list(map(int,input().split()))
m1,m2=(0,0),(0,0)
for i in range(n):
    x=(a[i],i+1)
    if x>m1:
        m2=m1
        m1=x
    elif x>m2:
        m2=x
print(m2[1])