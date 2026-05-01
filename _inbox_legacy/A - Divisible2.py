n,k=map(int,input().split())
a=list(map(int,input().split()))
for x in a:
    if x%k==0:
        print(x//k,end=" ")
print()