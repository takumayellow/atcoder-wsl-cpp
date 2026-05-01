n=int(input())
l=[element for row in[list(map(int,input().split()))for _ in range(n-1)]for element in row]
for i in range(1,n+1):
    if l.count(i)==n-1:print('Yes');break
else:print('No')