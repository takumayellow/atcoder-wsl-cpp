N = int(input())
A = list(map(int, input().split()))
Sum = 0
for i in range(N):
  Sum += A[i]
print(Sum)