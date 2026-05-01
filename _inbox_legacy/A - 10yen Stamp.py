x,y=map(int,input().split())
import math
if x>=y:
    print(0)
else:
    print(math.ceil((y-x)/10))