h,w=map(int,input().split())
for i in range(h):
    a=list(map(int,input().split()))
    l=[]
    for j in range(w):
        if a[j]==0:l.append(".")
        else: l.append(chr(a[j]+64))
    print("".join(l))