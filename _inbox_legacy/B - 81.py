n = int(input())
print("NYoe s"[n in {i * j for i in range(1, 10) for j in range(1, 10)}::2])
