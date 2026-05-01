P=list(map(int,input().split()))
ans=[]
for p in P:
    ans.append(chr(p+96))

print(*ans,sep="")