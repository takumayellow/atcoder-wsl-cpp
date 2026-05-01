n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print('NYoe s'[sum(a[i]*b[i] for i in range(n))==0::2])