s=list(input())
a=[]
s.pop(0)
while len(s)>1:
    c=0
    while s[0]=="-":
        c+=1
        s.pop(0)
    a.append(c)
    s.pop(0)
print(*a)