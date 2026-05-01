n=int(input())
s=[["0" for j in range(n)] for i in range(n)]
for i in range(n):
    j=n-i
    if i<=j:
        for k in range(i,j):
            for l in range(i,j):
                if s[k][l]=="0":
                    if i%2!=1:s[k][l]="#"
                    else: s[k][l]="."
                elif s[k][l]==".":
                    if i%2!=1:s[k][l]="#"
                else: 
                    if i%2!=0:s[k][l]="."
for i in range(n):
    print("".join(s[i]))