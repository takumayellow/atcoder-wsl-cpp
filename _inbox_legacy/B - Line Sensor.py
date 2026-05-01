h,w=map(int,input().split())
c=[input().split() for _ in range(h)]
import numpy as np
c1=np.char.replace(c,"#","0")
c=np.char.replace(c1,".","1")
c=[[int(e)for e in l]for l in c]
print(c)
for i in range(h):
    print(list(str(c[i])))
    print(len(list(str(c[i]))))
    for j in range(len(list(str(c[i])))):
        
        print(c)
""" for j in range(w): """
