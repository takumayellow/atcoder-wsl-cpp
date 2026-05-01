def fib1(n):
    return 1 if n<=1 else fib1(n-1)+fib1(n-2)
print(fib1(30))