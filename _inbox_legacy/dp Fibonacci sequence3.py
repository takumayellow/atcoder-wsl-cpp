def fib3(n):
    a=[1]*(n+1)
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]
print(fib3(30))