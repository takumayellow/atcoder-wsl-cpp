n=int(input())
sum=0
for i in range(n+1):
    sum+=((-1)**i)*(i**3)
print(sum)