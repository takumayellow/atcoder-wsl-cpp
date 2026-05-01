n,x=map(int,input().split())
s=""
for i in range(26):
    s+=n*chr(65+i)
print(s[x-1])