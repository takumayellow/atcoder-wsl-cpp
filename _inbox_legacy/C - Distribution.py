N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
for i in range(N*2):
    T[(i+1)%N] = min(T[(i+1)%N], T[i%N] + S[i%N])
for ans in T:
    print(ans)