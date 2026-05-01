n = int(input())
pos = [-1, -1] # 0: left, 1: right
ans = 0
for i in range(n):
    a, s = input().split()
    a = int(a)
    hand = (0 if s== 'L' else 1)
    if pos[hand] != -1:
        ans += abs(pos[hand] - a)
    pos[hand] = a
print(ans)