memo=[0]*(50)
def fib2(n):
    if n<=1:
        return 1
    else:
        if memo[n]==0:
            memo[n]=fib2(n-1)+fib2(n-2)
        return memo[n]
    
print(fib2(30))