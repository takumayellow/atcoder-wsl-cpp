n,k=map(int,input().split())
s=input()
t=[]
c=0
for i in range(n):
    if s[i]=="o"and c<k:t.append("o");c+=1
    else: t.append("x")
print(*t,sep="")