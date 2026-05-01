n=int(input())
s=input()
c=0
for i in range(n-2):
    if s[i]=="#"and s[i+2]=="#" and s[i+1]==".":c+=1
print(c)