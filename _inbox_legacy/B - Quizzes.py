n,x=map(int,input().split())
s=input()
c=x
for i in range(n):
    if s[i]=="o":c+=1
    elif c!=0: c-=1
print(c)