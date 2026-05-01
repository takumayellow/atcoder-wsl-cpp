n,x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def solve(c,z):
    c.sort(reverse=True)
    s=0
    for i in range(len(c)):
        s+=c[i]
        if s>z:
            return i+1
    return len(c)
print(min(solve(a,x),solve(b,y)))