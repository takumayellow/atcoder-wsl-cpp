def results(n):
    kicks = ''
    for i in range(1,n+1):
        if i % 3 == 0:
            kicks += 'x'
        else:
            kicks += 'o'
    return kicks

n = int(input())
print(results(n))