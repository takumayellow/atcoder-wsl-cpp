n,m=map(int,input().split())
P=0
for i in range(m):
    ai, bi = map(int,input().split())
    P+=ai*bi
print(P)