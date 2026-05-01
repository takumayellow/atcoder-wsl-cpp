import math

b = int(input())

# A^A = B を満たす A を探す
for a in range(1, int(math.log(b, 2)) + 2):  # A の範囲を制限する
    if a**a == b:
        print(a)
        break
else:
    print(-1)