N=int(input())
for i in range(N//1000):
  x=1000*i
  if N-x<1000:print(N-x);break