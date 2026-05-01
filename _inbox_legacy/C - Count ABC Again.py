n,q=map(int,input().split())
s=input()
list=[]
for i in range(q):
    x, c = input().split()
    x = int(x)
    s=s.replace(s[x-1],c)
    count=0
    for l in range(len(s)-2):
        if s[l]+s[l+1]+s[l+2]=="ABC":count+=1
    list.append(count)
print(*list,sep="\n")