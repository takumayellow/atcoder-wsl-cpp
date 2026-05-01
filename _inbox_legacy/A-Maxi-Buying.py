import math
N = int(input())
P = math.floor(1.08*N)
if P < 206:
    print("Yay!")
elif P == 206:
    print("so-so")
else:
    print(":(")