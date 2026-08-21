s = input()
l = len(s)
for i in range(l):
    for j in range(i,l):
        if 'keyence' == (s[:i]+s[j:]):
            print('YES')
            exit()
print('NO')
