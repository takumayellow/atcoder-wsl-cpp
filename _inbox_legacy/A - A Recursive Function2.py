def factorial_naive(n: int) -> int:
    result=1
    for i in range(n):
        result*=i+1
    return result
print(factorial_naive(int(input())))