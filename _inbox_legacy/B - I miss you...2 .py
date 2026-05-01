s = input()
new_s = ""
for x in s:
    new_s += x.replace(x, "x")
print(new_s)