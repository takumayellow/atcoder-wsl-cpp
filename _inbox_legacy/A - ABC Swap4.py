l=input().split()
print(*[l[(i-1)%len(l)] for i in range(len(l))])