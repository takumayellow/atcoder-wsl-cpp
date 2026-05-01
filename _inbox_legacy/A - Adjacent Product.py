n = int(input())
a = list(map(int, input().split()))
print(' '.join(str(a[i] * a[i + 1]) for i in range(n - 1)))