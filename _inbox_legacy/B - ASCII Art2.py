h, w = map(int, input().split())
m = []
for i in range(h):
    a = list(map(int, input().split()))
    l = []
    for j in range(w):
        if a[j] == 0:
            l.append(".")
        else:
            l.append(chr(a[j] + 64))
    m.append("".join(l))
print(*m, sep="\n")