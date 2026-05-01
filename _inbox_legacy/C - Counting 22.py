from bisect import bisect_left
n,q=map(int,input().split())
a=list(map(int,input().split()))
queries=[int(input()) for _ in range(q)]
a.sort()
results=[]
for x in queries:
    index=bisect_left(a,x)
    count=n-index
    results.append(count)
print("\n".join(map(str,results)))