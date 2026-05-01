s=input()
t=input()
if len(s)!=len(t):
    if len(s)>len(t):
        for i in range(len(t)):
            if s[i]!=t[i]:print(i+1);break
        else:print(len(t)+1)
    else:
        for i in range(len(s)):
            if s[i]!=t[i]:print(i+1);break
        else:print(len(s)+1)
else:
    for i in range(len(s)):
        if s[i]!=t[i]:print(i+1);break
    else:print(0)