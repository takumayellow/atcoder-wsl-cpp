N = int(input())
S = input()

dict_c = {'B':0,'W':1,'R':2}
mod = 3

answer = 0
C = 1
p = pow(2,N-1,mod)
three = 0
for i in range(N):
  if i>0:
    j = N-i
    while j%3==0:
      three += 1
      j //= 3
    k = i
    while k%3==0:
      three -= 1
      k //= 3
    C = (C*j*k)%mod
  if three>0:
    continue
  answer = (answer+C*p*dict_c[S[i]])%mod

if answer==0:
  print('B')
elif answer==1:
  print('W')
else:
  print('R')