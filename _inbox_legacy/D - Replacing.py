from itertools import groupby
import bisect

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append([k, int(len(list(v)))])
    return res

n=int(input())
a=list(map(int,input().split()))
q=int(input())
a=sorted(a)
a=runLengthEncode(a)
x=[]
for i in range(n):
    if i<=len(a)-1:x.append((a[i])[0])
for _ in range(q):
    b,c=map(int,input().split())
    index=bisect.bisect(x,b)
    if c in x:
        id=bisect.bisect(x,c)
        a[id-1][1]+=a[index-1][1]
        a[index-1][1]=0
    else:
        id=bisect.bisect(x,c)
        a.insert(id,[c,a[id-1][1]])
        a[index-1][1]=0
        x.append(c)
        x=sorted(x)
    print(sum(a[i][0]*a[i][1] for i in range(len(a))))