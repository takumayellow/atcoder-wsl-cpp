a,b,c=map(int,input().split())
print('NYoe s'[(a-b)*(b-c)*(c-a)>0::2])