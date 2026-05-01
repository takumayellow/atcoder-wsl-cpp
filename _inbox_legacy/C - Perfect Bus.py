n = int(input())
a = list(map(int, input().split()))
s,m=0,0
for x in a:s+=x;m=min(m,s)
print(s-m)