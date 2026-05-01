s=input()
for i in range(len(s)):
    if ord(s[i])<95:
        print(i+1)
        break