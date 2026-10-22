n, k = map(int,input().split())
input=list(map(int,input().split()))
a = [0]*k
for i in range(n):
    a[input[i]-1]+=1
b = list(set(a))
if len(set(b)) == 1: print(a.count(b[-1]))
elif b[-2] == b[-1] - 1:print(a.count(b[-1]) + a.count(b[-2]))
else: print(a.count(b[-1]))
