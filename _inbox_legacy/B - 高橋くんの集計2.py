n=int(input())
l=list(map(int,input().split()))
e=sum(l)//(n-l.count(0))
print(e+1*(sum(l)%(n-l.count(0))!=0))