n,k=map(int,input().split())
r=list(map(int,input().split()))
def f(i,a):
    if i==n:
        if sum(a)%k==0:
            print(" ".join(map(str,a)))
    else:
        for j in range(1,r[i]+1):
            a.append(j)
            f(i+1,a)
            a.pop()
f(0,[])