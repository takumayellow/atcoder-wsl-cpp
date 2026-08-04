import sys
input = sys.stdin.readline


while True:
    n = int(input())
    if n == 0: break

    list = []

    for i in range(n):
        s = int(input())
        list.append(s)

    list = sorted(list)
    list = list[1:-1]

    ave = sum(list)//(n-2)

    print(ave)
