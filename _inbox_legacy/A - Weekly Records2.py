N=int(input())
A=list(map(int,input().split()))
ans=[sum(A[7*i:7*(i+1)]) for i in range(N)]
print(*ans)