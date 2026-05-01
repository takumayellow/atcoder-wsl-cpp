n=int(input())
x=bin(n)
c=0
for i in range(1,len(x)):
    if x[-i]=="0":c+=1
    else:break
print(c)