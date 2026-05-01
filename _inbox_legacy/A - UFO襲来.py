s=list(input())
c=0
for i in range(9):
    if s[i]=="Z" and s[i+1]=="O" and s[i+2]=="N" and s[i+3]=="e":
        c+=1
print(c)