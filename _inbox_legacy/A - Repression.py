numlist=list(map(int,input().split()))
snlist=sorted(numlist)
slist=snlist[-2:]
print(sum(slist))