import numpy as np
m=int(input())
t=np.base_repr(m,3)[::-1]
a=[]
for i in range(len(t)):
    for _ in range(int(t[i])):a.append(i)
print(len(a))
print(*a)