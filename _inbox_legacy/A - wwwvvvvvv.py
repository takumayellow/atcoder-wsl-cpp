P=0
S=input()
for i in range(len(S)):
    if S[i]=="v": P+=1
    else: P+=2
print(P)