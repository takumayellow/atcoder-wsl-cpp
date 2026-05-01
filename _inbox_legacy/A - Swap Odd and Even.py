s = input()
for i in range(len(s) // 2 - 2):
    s = s.replace(s[2 * i + 1], "_").replace(s[2 * i + 2], s[2 * i + 1]).replace("_", s[2 * i + 2])
print(s)