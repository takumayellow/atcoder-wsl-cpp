s,t=input().split()
for w in range(1,len(s)):
    for c in range(w):
        l=[]
        for i in range(c,len(s),w):
            l.append(s[i])
        if "".join(l)==t:
            print("Yes")
            exit()
print("No")