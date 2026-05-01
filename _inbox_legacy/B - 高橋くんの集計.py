n=int(input())
l=list(map(int,input().split()))
import math
print(math.ceil(sum(l)/(n-l.count(0))))