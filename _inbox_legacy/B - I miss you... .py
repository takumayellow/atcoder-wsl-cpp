s=list(input())
for i in range(len(s)):
    s[i]="x"
print(*s,sep="")