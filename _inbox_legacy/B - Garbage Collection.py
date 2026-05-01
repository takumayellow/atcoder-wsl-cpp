n=int(input())
q,r=map(list, zip(*[list(map(int, input().split())) for _ in range(n)]))
Q=int(input())
t,d=map(list, zip(*[list(map(int, input().split())) for _ in range(Q)]))
for j in range(Q):
    print(d[j]+(r[t[j]-1]-d[j])%q[t[j]-1])