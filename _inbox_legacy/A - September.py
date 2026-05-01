s=[input().strip() for _ in range(12)]
c=0
for i in range(12):
    if len(s[i])==i+1:c+=1
print(c)