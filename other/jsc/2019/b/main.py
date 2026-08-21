n, k = map(int,input().split())
a = list(map(int,input().split()))

MOD = 10 ** 9 + 7

cnt1 = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]: cnt1 += 1

cnt2 = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] < a[j]: cnt2 += 1

term1 = (k * (k+1) // 2) % MOD
term2 = (k * (k-1) // 2) % MOD

ans = (cnt1 * term1 + cnt2 * term2) % MOD

print(ans)
