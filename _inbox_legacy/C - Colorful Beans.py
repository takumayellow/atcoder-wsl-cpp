n=int(input())
comb={}
for _ in range(n):
    a,c=map(int,input().split())
    if comb.get(c):comb[c]=min(comb[c],a)
    else:comb[c]=a
print(max(comb.values()))