n=int(input())
a=list(map(int,input().split()))
q=int(input())
l=[]
for i in range(q):
    s=list(map(int,input().split()))
    if s[0]==1:a[s[1]-1]=s[2]
    if s[0]==2:l.append(a[s[1]-1])
print(*l, sep='\n')