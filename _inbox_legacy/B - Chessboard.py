n=8
s=[input() for i in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j]=="*":
            print(chr(ord("a")+j)+str(n-i))