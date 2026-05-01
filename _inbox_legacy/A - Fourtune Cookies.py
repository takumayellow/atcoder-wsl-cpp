a,b,c,d=map(int,input().split())
s=[a,b,c,d]
s=sorted(s)
if s[0]+s[3]==s[1]+s[2]:print("Yes")
elif s[3]==s[0]+s[1]+s[2]:print("Yes")
else: print("No")