n,h,x=map(int,input().split())
plist=list(map(int,input().split()))
for i in range(n):
    P=plist[i]
    if h+P>=x:
        break
    else: i = i+1
print(i+1)