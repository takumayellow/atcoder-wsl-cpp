from bisect import bisect_left

N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [int(input()) for _ in range(Q)]

A.sort()

results = []
for x in queries:
    index = bisect_left(A, x)
    count = N - index
    results.append(count)

print('\n'.join(map(str, results)))