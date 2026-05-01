l, r = map(int, input().split())
p = list("atcoder")
x = []
for i in range(l-1, r):
    x.append(p[i])
print(''.join(x))