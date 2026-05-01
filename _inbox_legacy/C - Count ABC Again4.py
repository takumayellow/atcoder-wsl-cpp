n,q=map(int,input().split())
s=list(".."+input()+"..")
cnt=0
for i in range(n+2):
    cnt+=s[i:i+3]==["A","B","C"]
for _ in range(q):
    x,c=input().split()
    x=int(x)-1+2
    for i in range(x-2,x+1):
        cnt-=s[i:i+3]==["A","B","C"]
    s[x]=c
    for i in range(x-2,x+1):
        cnt+=s[i:i+3]==["A","B","C"]
    print(cnt)