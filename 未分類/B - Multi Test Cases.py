t = int(input())
for _ in range(t):
    input()  # N を読み捨て
    print(sum(int(x) % 2 for x in input().split()))
