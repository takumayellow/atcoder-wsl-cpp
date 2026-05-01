n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    for j in range(i+1,n):
        if a[i]==a[j]:s.append(j-i+1);break
if s==[]:s.append(-1)
print(*s)