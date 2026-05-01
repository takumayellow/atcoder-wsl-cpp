n=int(input())
s=list(map(int,input().split()))
a=[s[0]]
for i in range(n-1):
    a.append(s[i+1]-s[i])
print(*a)