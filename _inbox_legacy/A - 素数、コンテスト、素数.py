n = int(input())
c = 0
for i in range(1, n + 1):
    c += int(n % i == 0)
print("YNEOS"[c != 2::2])