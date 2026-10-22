n = int(input())
a = 1
s = 0
for i in range(1,n+1):
    s += sum(map(int, str(a)))
    a = s
print(s)
