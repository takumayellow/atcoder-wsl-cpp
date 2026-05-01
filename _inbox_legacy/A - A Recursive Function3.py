def fr(n:int)->int:
    if n==0:return 1
    return n*fr(n-1)
print(fr(4))