n=int(input())
d=[*map('BW'.find,input())]
e=1
while e<n: e*=3
while n>1:
  while n<=e: e//=3
  n-=e
  d=[-d[i]-d[i+e] for i in range(n)]
print('BWR'[d[0]%3])