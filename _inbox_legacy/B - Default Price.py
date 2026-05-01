n,m=map(int,input().split())
c=list(input().split())
d=list(input().split())
p_init=list(map(int,input().split()))
p0=p_init[0]
p=p_init[1:]
s=0
for i in range(n):
    if c[i] in d:
        s+=p[d.index(c[i])]
    else:s+=p0
print(s)

