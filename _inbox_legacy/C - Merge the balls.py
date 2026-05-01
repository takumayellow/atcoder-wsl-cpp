n=int(input())
a=list(map(int,input().split()))
s=[]
for x in a:
    s.append(x)
    while len(s)>=2 and s[-2]==s[-1]:
        x=s.pop()
        s.pop()
        s.append(x+1)
print(len(s))