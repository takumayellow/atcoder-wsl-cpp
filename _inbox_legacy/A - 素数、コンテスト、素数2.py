n=int(input())
ans=1
for i in range(2,min(10000,n)):
    if n%i==0:ans=0
if ans:print("YES")
else:print("NO")