import numpy as np

n=int(input())
a=list(map(float,input().split()))
a.sort()
print(np.mean(a[n:4*n]))
