n=int(input())
h=list(map(int,input().split()))
s=[]
ans=[]
for x in h[::-1]:
    ans.append(len(s))
    while s and s[-1]<x:
        s.pop()
    s.append(x)
print(*ans[::-1])