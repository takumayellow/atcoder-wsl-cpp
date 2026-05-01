s=input()
c=0
while len(s)>=2:
    c+=1
    s=s[:-2]
    if s[:len(s)//2]==s[len(s)//2:]:print(len(s));break    
