n=int(input())
a=list(map(int,input().split()))
print('NYoe s'[sorted(a)==list(range(1,n+1))::2])