h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
l=[]
for j in range(w):
    r=list(c[i][j] for i in range(h))
    l.append(r.count("#"))
print(*l)