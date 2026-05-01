a,b,c=map(int,input().split())
print('NYoe s'[(a-c)%24<(b-c)%24::2])