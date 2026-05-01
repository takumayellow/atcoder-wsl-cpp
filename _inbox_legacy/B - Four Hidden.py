t=input()
u=input()
flag=True
for j in range(0,len(t)-len(u)+1):
    for i in range(len(u)):
        if u[i]==t[j+i]or t[j+i]=="?":continue
        else:flag=False
if flag==False:print("Yes")
else: print("No")