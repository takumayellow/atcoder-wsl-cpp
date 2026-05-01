import math

def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    limit = int(math.sqrt(n)) + 1
    candidate = list(range(2, n + 1))
    prime = []
    
    while candidate:
        p = candidate[0]
        if p > limit:
            prime.extend(candidate)
            break
        prime.append(p)
        candidate = [x for x in candidate if x % p != 0]
    
    return prime

n = int(input())
primes_under_n = sieve_of_eratosthenes(n)
if n in primes_under_n:
    print("YES")
else:
    print("NO")