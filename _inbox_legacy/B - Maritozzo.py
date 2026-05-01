s = [input().strip() for _ in range(3)]
t = input()
for i in range(len(t)):
    if t[i] == '1':
        print(s[0], end="")
    elif t[i] == '2':
        print(s[1], end="")
    else:
        print(s[2], end="")