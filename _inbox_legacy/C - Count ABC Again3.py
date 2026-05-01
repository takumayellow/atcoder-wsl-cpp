n,q=map(int,input().split())
s=list(input())
for _ in range(q):
    x,c=input().split()
    x=int(x)-1
    s[x]=c
    cnt=0
    for i in range(n-2):
        cnt+=s[i:i+3]==["A","B","C"]
    print(cnt)