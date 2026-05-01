n,d=map(int,input().split())
s=input()
l=list(s)
for i in range(d):
    for j in range(n-1,-1,-1):
        if l[j]=="@":l[j]=".";break
print(*l,sep="")