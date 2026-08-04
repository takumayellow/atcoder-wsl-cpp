s = input()
t = []
for i in range(len(s)):
  if s[i] == '1': t.append(1)
  elif s[i] == '0': t.append(0)
  elif len(t) == 0: continue
  else: t.pop(-1)
print(*t, sep="")
