n=int(input())
x,y=map(list, zip(*[list(map(int, input().split())) for _ in range(n)]))
c=0
import math
for i in range(n-1):
    c+=math.sqrt((x[i]-x[i+1])**2+(y[i]-y[i+1])**2)
c+=math.sqrt((x[0])**2+(y[0])**2)
c+=math.sqrt((x[n-1])**2+(y[n-1])**2)
print(c)