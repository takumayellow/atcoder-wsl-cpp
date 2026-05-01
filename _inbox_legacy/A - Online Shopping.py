n,s,k=map(int,input().split())
P=0
for i in range(n):
    pi,qi=map(int,input().split())
    P+=pi*qi
if P>=s: print(P)
else: print(P+k)