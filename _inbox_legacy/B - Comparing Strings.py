a,b=map(int,input().split())
p=str(a)*b
q=str(b)*a
for i in range(min(a,b)):
    if p[i]!=q[i]:
        if p[i]<q[i]:print(p)
        else:print(q)
        break
    else:print(p);break